# Contract Simplifier AI

**Contract Simplifier AI** is a web app that helps users quickly understand complex legal contracts. It simplifies legal language into plain English bullet points and answers questions based on the uploaded contract — all powered by Together AI’s free large language models (LLMs).

![image](https://github.com/user-attachments/assets/24024649-2e19-4bf2-8752-05ee427a2f0f)
(https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png)

---

## 🚀 Features

- 🧠 AI-powered legal language simplification
- 📤 Upload any PDF contract
- 💬 Ask questions about contract clauses
- ⚡ Built with `Together AI` models (Mistral 7B)
- 🎯 Runs on `Streamlit` (frontend) + `Python` (backend)

---

## 🛠️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io)
- **LLM Backend**: [Together.ai](https://www.together.ai/)
- **PDF Parsing**: PyMuPDF (`fitz`)
- **Env Management**: `python-dotenv`
- **API Communication**: `requests`

---

## 📂 Project Structure
📁 contract-simplifier-ai/
│
├── app.py                 
├── requirements.txt        
└── .env

📦 Installation & Run Locally
git clone https://github.com/ananyavrm04/contract-simplifier-ai.git
cd contract-simplifier-ai
pip install -r requirements.txt
streamlit run app.py
