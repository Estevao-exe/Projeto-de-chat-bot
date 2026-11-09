# 🤖 Assistente Virtual de Saúde Inteligente

![Python](https://img.shields.io/badge/Python-Ready-blue)
![Artificial Intelligence](https://img.shields.io/badge/Artificial%20Intelligence-AI-purple)
![Project](https://img.shields.io/badge/Project-Academic-green)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

## 📌 Sobre o Projeto

Este repositório documenta o planejamento, a arquitetura e a engenharia de prompts por trás do desenvolvimento de um chatbot inteligente focado na área da saúde.

O projeto foi concebido utilizando ferramentas modernas de Inteligência Artificial e soluções *No-Code*, servindo como base de modelagem para uma futura implementação robusta em Python.

O objetivo é desenvolver um assistente virtual capaz de oferecer acolhimento inicial, compreender dúvidas relacionadas à saúde e fornecer orientações educativas de maneira segura e responsável.

---

## 🎯 O Problema e a Solução

### 🔍 O Desafio

O acesso a informações preliminares sobre saúde muitas vezes pode ser confuso para usuários sem conhecimento técnico.

Além disso, canais tradicionais de atendimento podem sofrer com sobrecarga, gerando filas de espera para dúvidas simples e orientações iniciais que poderiam ser automatizadas de forma segura.

### 💡 A Solução

Desenvolver um assistente virtual que:

- Realize o acolhimento inicial do usuário.
- Identifique informações básicas sobre sintomas por meio de perguntas direcionadas.
- Forneça orientações educativas e informativas.
- Reconheça possíveis situações de emergência.
- Oriente o usuário a procurar atendimento médico adequado sempre que necessário.

---

## 🏗️ Arquitetura do Sistema e Fluxo de Conversa

Mesmo sem a utilização de código tradicional nesta fase, a solução foi planejada seguindo a lógica de um fluxo estruturado de dados.

### Fluxo de funcionamento

1. **Entrada (Input):** O usuário relata uma dúvida ou sintoma por meio da interface de texto.
2. **Processamento (IA Engine):** O mecanismo de linguagem processa a mensagem utilizando regras e instruções previamente definidas (*System Prompts*).
3. **Validação de Segurança:** A IA verifica se a solicitação exige algum alerta crítico ou orientação de emergência.
4. **Saída (Output):** O chatbot fornece uma resposta humanizada, informativa e acompanhada de orientações de segurança.

> As instruções lógicas do sistema e os prompts estruturados utilizados estão armazenados na pasta `/prompts` deste repositório, para fins de organização e auditoria técnica.

---

## 🧠 Engenharia de Prompt Aplicada

Para garantir que a Inteligência Artificial se comporte de maneira ética e segura, especialmente por se tratar da área da saúde, a engenharia de prompts foi desenvolvida com base em quatro pilares:

- **Restrição de Escopo (Guardrails):** O chatbot não deve realizar diagnósticos definitivos nem prescrever medicamentos.
- **Tom de Voz:** Comunicação empática, acolhedora, objetiva e profissional.
- **Ações de Emergência:** Quando o usuário mencionar sintomas potencialmente graves, como dor intensa no peito ou falta de ar aguda, o sistema deve orientar a busca imediata por atendimento de emergência.
- **Autenticação por API:** O acesso ao chatbot depende de uma chave de API disponibilizada por meio da plataforma Groq (Groq API).

---

## 🔐 Autenticação e API

O funcionamento do chatbot depende de uma chave de API da Groq.

Para utilizar o sistema, é necessário possuir uma chave de acesso válida, disponibilizada pela plataforma oficial.

**Importante:** A chave de API é confidencial e não deve ser compartilhada publicamente ou enviada diretamente para repositórios do GitHub.

Recomenda-se armazenar as credenciais em variáveis de ambiente ou em um arquivo `.env`, devidamente incluído no `.gitignore`.

---

## 🚀 Próximos Passos — Evolução Técnica em Python

Como estudante de Ciência da Computação, o objetivo deste projeto é servir como uma especificação de requisitos para o desenvolvimento de uma aplicação real.

O planejamento técnico envolve:

- [ ] **Back-end com Python:** Migrar a lógica do chatbot para um servidor utilizando os frameworks FastAPI ou Flask.
- [ ] **Integração com APIs de LLM:** Conectar o código Python diretamente a modelos de linguagem por meio de APIs, utilizando bibliotecas apropriadas.
- [ ] **Banco de Dados:** Implementar um histórico de conversação seguro utilizando SQLite ou PostgreSQL.
- [ ] **Interface de Usuário:** Desenvolver uma interface intuitiva para facilitar a interação com o assistente.
- [ ] **Segurança:** Implementar mecanismos de proteção de dados e gerenciamento seguro de credenciais.

---

## ⚠️ Isenção de Responsabilidade Médica (Disclaimer)

**ATENÇÃO:** Este software é um projeto puramente acadêmico, experimental e de portfólio tecnológico.

- Este chatbot **NÃO** fornece diagnósticos médicos.
- Este chatbot **NÃO** prescreve tratamentos ou medicamentos.
- As interações possuem caráter estritamente educativo e informativo.
- As respostas do sistema não substituem consultas, exames ou avaliações realizadas por profissionais de saúde qualificados.
- Em caso de suspeita de problemas de saúde, procure orientação médica.
- Em situações de emergência, ligue para o **192 (SAMU)**.

---

## 👨‍💻 Autor

Desenvolvido por **Estevão** **Danie** **Nicolas**

*Estudante de Ciência da Computação, interessado em tecnologia, Inteligência Artificial e desenvolvimento de software.*

### 🔗 Contatos e Redes

<!--[LinkedIn](https://www.linkedin.com/in/estevão-figueiredo-garcia-8013963a3/)-->
  
- [GitHub Estevão](https://github.com/Estevão-exe)
- [GitHub Daniel](https://github.com/Danyel-xp)
- [GitHub Nicolas](https://github.com/NicoleswebMaster)

---

⭐ Se este projeto despertou seu interesse, considere deixar uma estrela no repositório!

**Desenvolvido com dedicação e foco em tecnologia e Inteligência Artificial.**
