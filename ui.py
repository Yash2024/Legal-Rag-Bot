import streamlit as st
import requests

st.title("⚖️ Legal RAG Chatbot (BNS)")

with st.form(key="query_form"):
    query = st.text_input("Ask your legal question")
    submit = st.form_submit_button("Ask")

if submit and query:
    res = requests.get(f"http://127.0.0.1:8000/ask?question={query}")
    
    data = res.json()
    
    st.write("### Answer")
    st.write(data["answer"])
    
    st.write("### Sources")
    for s in data.get("sources", []):
        st.write(s)