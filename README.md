# 🤖 Ask Your Document – Roberta QA App

A smart Streamlit app that lets you upload any `.pdf` or `.txt` file and ask intelligent questions from its content.  
Powered by 🤖 `deepset/roberta-base-squad2`, built using Hugging Face Transformers.

🔗 **Live App**: [CLICK TO RUN](https://askyourdocai-33wc8e6scqlcjdggsqc8uw.streamlit.app/)  
📦 **Supports**: PDF + TXT  
💡 **Built for**: Students, journalists, researchers, lawyers, curious humans

---

## 🚀 Features

- 📄 Upload any document (txt/pdf)
- 💬 Ask any natural language question
- 🧠 Roberta model finds best possible answer
- 💻 Powered by HuggingFace + Streamlit
- 🔁 Fully local and free (no OpenAI key needed)

---

## 🛠️ Technologies

| Tool | Role |
|------|------|
| `streamlit` | Web interface |
| `transformers` | BERT-based QA |
| `deepset/roberta-base-squad2` | Pretrained SQuAD2 model |
| `pdfplumber` | Extract text from PDF |
| `torch` | Backend for transformers |

---

## 📄 Sample Questions

After uploading a file, try:
- “What is the main objective of this report?”
- “Who is responsible for the policy change?”
- “What is the penalty mentioned?”
- “Which company leads the market?”

---

## 📁 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
