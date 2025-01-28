from dotenv import load_dotenv

load_dotenv()

from graph.graph import app
import streamlit as st
from streamlit_chat import message


st.header("Assistente de perguntas e respostas sobre a LGPD")

prompt = st.text_input("Prompt", placeholder="Digite sua pergunta aqui", key="prompt_input")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []
    
if prompt:
    print("PERGUNTA",prompt)
    with st.spinner("Generating response..."):
        generated_response = app.invoke(input={"question": prompt})
 
    formated_response = ( 
        f"{generated_response['generation']}" 
    )
    
    st.session_state["user_prompt_history"].append(prompt)
    st.session_state["chat_answers_history"].append(formated_response)

if st.session_state["chat_answers_history"]:
    for idx, (generated_response, user_query) in enumerate(zip(st.session_state["chat_answers_history"], st.session_state["user_prompt_history"])):
        message(user_query, is_user=True, key=f"user_message_{idx}")
        message(generated_response, key=f"response_message_{idx}")