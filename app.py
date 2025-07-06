import streamlit as st
import fitz  # PyMuPDF
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# ---- Helper Functions ----

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def summarize_contract(contract_text):
    prompt = f"""
You are a legal assistant. Read the following contract and explain it in bullet points in simple English:

{contract_text[:4000]}
"""

    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "system", "content": "You are a helpful legal assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 800
    }
    res = requests.post(url, headers=headers, json=data)
    return res.json()["choices"][0]["message"]["content"]

def answer_question(contract_text, user_question):
    prompt = f"""
Here is a legal contract:
{contract_text[:4000]}

Answer this question clearly and in simple terms:
{user_question}
"""

    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "system", "content": "You are a helpful legal assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 500
    }
    res = requests.post(url, headers=headers, json=data)
    return res.json()["choices"][0]["message"]["content"]

# ---- Streamlit UI ----

st.set_page_config(page_title="Contract Simplifier AI", layout="wide")
st.title("📜 Contract Simplifier AI")
st.markdown("Upload a legal contract and ask questions about it using a free Together AI LLM.")

uploaded_file = st.file_uploader("Upload a contract PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting and analyzing contract..."):
        contract_text = extract_text_from_pdf(uploaded_file)
        summary = summarize_contract(contract_text)

    st.subheader("📝 Simplified Summary")
    st.write(summary)

    st.subheader("💬 Ask a question about this contract")
    user_question = st.text_input("Your question:")

    if user_question:
        with st.spinner("Thinking..."):
            answer = answer_question(contract_text, user_question)
        st.success(answer)
