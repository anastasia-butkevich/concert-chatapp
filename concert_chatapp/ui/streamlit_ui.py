import streamlit as st
import requests
from concert_chatapp.settings.settings import API_URL


st.set_page_config(page_title="Concert Tour RAG", layout="centered")
st.title("Concert Tour RAG Assistant")

tab1, tab2 = st.tabs(["Ingest Document", "Ask a Question"])

with tab1:
    doc_input = st.text_area("Paste document:", height=250)
    if st.button("Submit Document"):
        if not doc_input.strip():
            st.warning("Please enter text.")
        else:
            res = requests.post(f"{API_URL}/ingest", json={"doc_input": doc_input})
            if res.ok:
                data = res.json()
                st.success(data["message"])
                st.markdown(f"**Summary:** {data['summary'][0]}")
            else:
                st.error("Ingest failed.")

with tab2:
    usr_input = st.text_input("Ask a question:")
    if st.button("Ask"):
        if not usr_input.strip():
            st.warning("Please enter a question.")
        else:
            res = requests.post(f"{API_URL}/chat", json={"usr_input": usr_input})
            if res.ok:
                st.markdown(f"**Answer:** {res.json()['answer']['content']}")
            else:
                st.error("Chat failed.")
