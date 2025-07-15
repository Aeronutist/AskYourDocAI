import torch
import streamlit as st
from transformers import pipeline
import pdfplumber
import os

# Load model once
@st.cache_resource
def load_model():
    return pipeline("question-answering",model="deepset/roberta-base-squad2")

qa_pipeline = load_model()

st.set_page_config(page_title="Ask Your Doc AI", layout="centered")

st.title("📄 Ask Your Document – BERT QA App")
st.markdown("Upload a `.pdf` or `.txt` file and ask anything about its content!")

# Upload file
uploaded_file = st.file_uploader("📁 Upload your document", type=["pdf", "txt"])

if uploaded_file:
    ext = os.path.splitext(uploaded_file.name)[-1].lower()
    
    if ext == ".txt":
        context = uploaded_file.read().decode("utf-8")
    elif ext == ".pdf":
        pdf_context = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    pdf_context += text
        context = pdf_context
    else:
        st.error("❌ Unsupported file format.")
        st.stop()

    st.success("✅ Document loaded successfully!")

    question = st.text_input("💬 Ask a question from the document:")

    if question and context:
        with st.spinner("🤖 Thinking..."):
            try:
                result = qa_pipeline(question=question, context=context)
                st.markdown(f"### 🧠 Answer: `{result['answer']}`")
            except Exception as e:
                st.error(f"❌ Failed to answer: {str(e)}")
                
