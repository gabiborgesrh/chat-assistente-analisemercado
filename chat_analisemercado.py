import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("OPENAI_ASSISTANT_ID")

st.set_page_config(page_title="Assistente de Análise de Mercado", layout="wide")
st.title("💬 Chat com sua Assistente de Análise de Mercado")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Envie sua análise, pedido de currículo, texto do LinkedIn...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        msg_placeholder.markdown("⌛ Pensando...")

        thread = openai.beta.threads.create()
        openai.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt
        )
        run = openai.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        while True:
            run_status = openai.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run_status.status == "completed":
                break

        messages = openai.beta.threads.messages.list(thread_id=thread.id)
        reply = messages.data[0].content[0].text.value

        msg_placeholder.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
