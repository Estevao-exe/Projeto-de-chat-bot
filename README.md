# Projeto-de-chat-bot
# 🤖 Assistente Virtual de Saúde Inteligente

[![No-Code](https://shields.io)](#)
[![Python-Ready](https://shields.io)](#)
[![Context](https://shields.io)](#)

Este repositório documenta o planejamento, a arquitetura e a engenharia de prompts por trás do desenvolvimento de um chatbot inteligente focado em saúde. O projeto foi concebido utilizando ferramentas modernas de Inteligência Artificial e soluções *No-Code*, servindo como base de modelagem para uma futura implementação robusta em Python.

---

## 📌 O Problema e a Solução

### O Desafio
O acesso a informações preliminares sobre saúde muitas vezes é confuso para o usuário comum. Canais de atendimento tradicionais sofrem com sobrecarga, gerando filas de espera para dúvidas simples e triagens iniciais que poderiam ser automatizadas de forma segura.

### A Solução
Um assistente virtual que realiza o acolhimento inicial do usuário, filtra informações básicas de sintomas através de perguntas direcionadas e fornece orientações educacionais rápidas, direcionando o paciente para o serviço médico adequado sempre que necessário.

---

## 🛠️ Arquitetura do Sistema & Fluxo de Conversa

Mesmo sem o uso de código tradicional nesta fase, a solução foi desenhada seguindo a lógica de um fluxo estruturado de dados:

1. **Entrada (Input):** O usuário relata uma dúvida ou sintoma na interface de texto.
2. **Processamento (Engine de IA):** O motor de linguagem processa a mensagem sob a camada de regras pré-definidas (System Prompts).
3. **Validação de Segurança:** A IA verifica se a solicitação exige um alerta crítico de emergência.
4. **Saída (Output):** O bot entrega uma resposta humanizada, puramente informativa, acompanhada de alertas de segurança.

*As instruções lógicas do sistema e os prompts estruturados utilizados estão salvos na pasta `/prompts` deste repositório para fins de auditoria técnica.*

---

## 🧠 Engenharia de Prompt Aplicada

Para garantir que a IA se comporte de maneira ética e segura (essencial na área da saúde), a engenharia de instrução foi baseada em três pilares:

* **Restrição de Escopo (Guardrails):** O bot foi programado para recusar tentativas de diagnósticos definitivos ou prescrição de medicamentos.
* **Tom de Voz:** Empático, acolhedor, direto e estritamente profissional.
* **Ações de Emergência:** Caso o usuário mencione sintomas de alta gravidade (como dor forte no peito ou falta de ar aguda), o fluxo intercepta a conversa e instrui a busca imediata por um pronto-socorro.
* **você so pode acessar o chat-bot com uma chaveAPI, que é disponibilizada no GROQ_API**

---

## 🚀 Próximos Passos (Evolução Técnica em Python)

Como estudante de Ciência da Computação, o objetivo deste projeto é servir de especificação de requisitos para uma aplicação real. O plano de desenvolvimento técnico envolve:

- [ ] **Back-end com Python:** Migrar a lógica do chatbot para um servidor utilizando o framework **FastAPI** ou **Flask**.
- [ ] **Integração de APIs de LLM:** Conectar o script Python diretamente à API da OpenAI ou Anthropic utilizando a biblioteca oficial ou o framework **LangChain**.
- [ ] **Banco de Dados:** Implementar um histórico de conversação seguro para o usuário utilizando SQLite ou PostgreSQL.

---

## ⚠️ Isenção de Responsabilidade Médica (Disclaimer)

**ATENÇÃO:** Este software é um projeto puramente acadêmico, experimental e de portfólio de tecnologia. 
* Este chatbot **NÃO** fornece diagnósticos médicos.
* Este chatbot **NÃO** prescreve tratamentos ou medicações.
* As interações têm caráter estritamente educativo e informativo. 
* Em caso de suspeita de problemas de saúde, procure sempre um médico ou profissional de saúde qualificado. Em caso de emergência, ligue para o 192 (SAMU).

---

## 👤 Autor

Desenvolvido por **Estevão**  
*Estudante de Ciência da Computação em evolução constante.*

* [Meu LinkedIn]([www.linkedin.com/in/estevão-figueiredo-garcia-8013963a3])
* [Meu Perfil GitHub](https://github.com [Estevão-exe])
