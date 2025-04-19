import openai
import streamlit as st

# Configuração da chave da API do OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Função para gerar resposta usando o modelo GPT-3.5 ou GPT-4
def get_assistant_response(user_input):
    try:
        # Enviando a mensagem do usuário para a API do OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ou "gpt-4", dependendo do seu plano
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": user_input}
            ]
        )
        # Extraindo a resposta do modelo
        assistant_message = response['choices'][0]['message']['content']
        return assistant_message
    except Exception as e:
        return f"Erro ao obter resposta: {e}"

# Interface do Streamlit
st.title("Chat Assistente - Análise de Mercado e Carreira")

# Caixa de entrada de texto para o usuário
user_input = st.text_input("Envie sua pergunta ou análise:")

# Se o usuário enviar uma pergunta
if user_input:
    response = get_assistant_response(user_input)
    st.write("Assistente:", response)
