

# Interactive QA System

This is a Streamlit-based interactive Question Answering (QA) system that allows users to upload PDF question papers. The system processes the PDF, extracts text, splits the data into smaller chunks, creates vector embeddings, and stores the embeddings in a FAISS index. The user can then query the system, and it will retrieve relevant answers from the uploaded document.

## Features

- Upload a PDF question paper.
- Extract text from the PDF document.
- Split the text into smaller chunks for better processing.
- Create vector embeddings using OpenAI's language model.
- Store the embeddings in a FAISS index for efficient search.
- Query the system to get answers based on the uploaded document.

## Requirements

- Python 3.7+
- Streamlit
- PyPDF2
- langchain
- langchain_openai
- OpenAI API
- dotenv
- FAISS

To install the required libraries, you can use the following command:

```bash
pip install streamlit PyPDF2 langchain langchain_openai openai faiss-cpu dotenv


