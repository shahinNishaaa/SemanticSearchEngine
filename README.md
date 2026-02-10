# Semantic Search Engine for Academic PDFs

A Streamlit-based web application that allows users to perform semantic search on academic PDF documents using NLP embeddings.

## Features
- Upload and process academic PDFs
- Chunk text and generate semantic embeddings
- Perform meaning-based search (not keyword search)
- Simple and interactive Streamlit UI

## Tech Stack
- Python
- Streamlit
- pdfplumber
- Sentence Transformers
- FAISS (or whichever index you used)

## Project Structure
semantic-search-pdf/
├── app.py
├── pdf_utils.py
├── embed_utils.py
├── data/
│   └── sample.pdf
├── requirements.txt
├── README.md

## Setup Instructions

1. Clone the repository
```bash
git clone <repo-link>
cd SemanticSearchEngine
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
streamlit run app.py
```

