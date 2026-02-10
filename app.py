
import os
import streamlit as st
from pdf_utils import extract_text_from_pdf, chunk_text
from embed_utils import create_embeddings, build_faiss_index, semantic_search

st.title("Semantic Search Engine for Academic PDFs")

PDF_DIR = "data"

@st.cache_data
def prepare_data():
    text = ""
    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            text += extract_text_from_pdf(os.path.join(PDF_DIR, file))
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)
    index = build_faiss_index(embeddings)
    return chunks, index

chunks, index = prepare_data()

query = st.text_input("Ask a question from the PDFs")

if query:
    results = semantic_search(query, chunks, index)
    for i, res in enumerate(results):
        st.markdown(f"**Result {i+1}**")
        st.write(res)
        st.write("---")