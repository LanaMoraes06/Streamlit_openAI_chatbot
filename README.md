# # ChatBot Inteligente com IA (OpenAI + Streamlit) 🤖💬

Este projeto consiste numa aplicação web interactiva de ChatBot, desenvolvida em **Python**. A aplicação utiliza a API da **OpenAI** para gerar respostas inteligentes em tempo real e a framework **Streamlit** para construir uma interface de utilizador fluida e amigável.



## 🚀 Tecnologias Utilizadas

* **Python**
* **Streamlit** (Criação do frontend/interface web de forma rápida)
* **OpenAI API** (Integração com modelos de Inteligência Artificial)

## 📁 Estrutura dos Ficheiros

* `main.py`: Ficheiro principal da aplicação. Contém a lógica de interface com o Streamlit, o sistema de memória da conversa (`session_state`) e a comunicação com a API da OpenAI.
* `auxiliar.py`: Ficheiro de apoio utilizado para compreender e estruturar a manipulação de listas e dicionários, essenciais para gerir o histórico de mensagens (modelo de *roles*: "user" e "IA").

## ⚙️ Funcionalidades

* Interface de chat intuitiva e responsiva.
* Histórico de conversa: O bot possui "memória" e lembra-se do contexto das mensagens anteriores graças ao `session_state` do Streamlit.
* Integração direta com a inteligência artificial generativa.

## 🛠️ Como executar o projeto na sua máquina

1. Certifique-se de que tem o Python instalado.
2. Instale as bibliotecas necessárias através do terminal:
```bash
pip install streamlit openai
```
Configure a sua chave da API da OpenAI (Recomenda-se o uso de variáveis de ambiente para segurança).

Execute a aplicação com o comando:
```bash
streamlit run main.py
