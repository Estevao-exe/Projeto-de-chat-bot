import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# 🔹 Configuração
os.environ["USER_AGENT"] = "NutriBotPro/1.0"
os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY_HERE"  # Substitua pela sua chave de API da Groq


# 🔥 MODELO
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2
)


# 🌍 BASE DE CONHECIMENTO (ATUALIZADA E COMPLETA)
urls = [
    # 🇧🇷 Brasil
    "https://www.gov.br/saude/pt-br/composicao/saps/promocao-da-saude/guias-alimentares",

    # 🌍 OMS
    "https://www.who.int/news-room/fact-sheets/detail/healthy-diet",
    "https://www.who.int/health-topics/micronutrients",

    # 🌍 FAO
    "https://www.fao.org/nutrition/education/food-dietary-guidelines/en/",

    # 🧪 NIH
    "https://ods.od.nih.gov/factsheets/list-all/",

    # 🏥 CDC
    "https://www.cdc.gov/nutrition/index.html",

    # 🎓 Harvard
    "https://www.hsph.harvard.edu/nutritionsource/"
]


print("\n🔄 Carregando base de nutrição avançada...")

loader = WebBaseLoader(urls)
docs = loader.load()


# 🔹 Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=300
)

docs_split = splitter.split_documents(docs)


# 🔹 Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

vectorstore = FAISS.from_documents(docs_split, embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 6})


print("✅ Base carregada com sucesso!")


# 🧠 MEMÓRIA
memoria = []


# 🔹 PROMPT PROFISSIONAL
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """Você é um especialista em nutrição clínica, esportiva e saúde pública.

Você utiliza evidências científicas de:
- Ministério da Saúde do Brasil
- OMS (WHO)
- FAO
- NIH
- CDC
- Harvard

REGRAS:
- Use apenas o contexto fornecido
- Seja claro, técnico quando necessário e didático
- Diferencie evidência científica de opinião popular
- Não invente informações
- Se não souber, diga que não há informação suficiente
"""),

    ("user",
     """Histórico da conversa:
{historico}

Contexto científico:
{contexto}

Pergunta:
{pergunta}
""")
])

chain = prompt | llm


# 🔹 Função utilitária
def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)


# 🔥 INTERFACE CLI
print("\n" + "=" * 70)
print("🥗 NUTRIÇÃO IA PRO (BASE CIENTÍFICA GLOBAL)")
print("Digite 'sair' para encerrar")
print("=" * 70)


while True:
    pergunta = input("\n🧑 Você: ")

    if pergunta.lower() == "sair":
        print("\n👋 Encerrando...")
        break


    # 🔎 RAG
    docs_encontrados = retriever.invoke(pergunta)
    contexto = format_docs(docs_encontrados)


    # 🧠 memória curta
    memoria.append(f"Usuário: {pergunta}")
    historico = "\n".join(memoria[-8:])


    print("\n🤖 Processando evidências científicas...\n")

    resposta = chain.invoke({
        "historico": historico,
        "contexto": contexto,
        "pergunta": pergunta
    })


    memoria.append(f"Assistente: {resposta.content}")


    print("🤖 Nutrição IA Pro:")
    print(resposta.content)
    print("-" * 70)