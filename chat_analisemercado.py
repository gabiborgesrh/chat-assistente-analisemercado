import openai
import streamlit as st

# Configuração da chave de API
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Função para obter resposta do modelo GPT
def obter_resposta(prompt):
    try:
        # Chamada para o modelo GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",  # ou "gpt-3.5-turbo" se preferir outro modelo
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
        return None

# Interface do Streamlit
st.title("Chat Assistente de Análise de Mercado")

# Solicitar entrada do usuário
user_input = st.text_input("Digite seu prompt:")

if user_input:
    resposta = obter_resposta(user_input)
    if resposta:
        st.write("Resposta do Assistente:", resposta)
