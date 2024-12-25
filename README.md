# Interactive QA System

This is a Streamlit-based interactive Question Answering (QA) system that allows users to upload PDF question papers. The system processes the PDF, extracts text, splits the data into smaller chunks, creates vector embeddings, and stores the embeddings in a FAISS index. The user can then query the system, and it will retrieve relevant answers from the uploaded document.

![Interactive QA system](https://github.com/user-attachments/assets/0aca9762-a3dd-4b72-b41f-f1cb25047811)

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
```
# Setup
- Clone the repository or download the code.

- Update the .env file in the root directory of the project to store your OpenAI API key

- Run the Streamlit app:
```bash
streamlit run app.py
```
- Open the app in your browser, usually at http://localhost:8501.


# How to Use

- Upload Question Paper:  In the sidebar, click on "Upload Question Paper" to upload a PDF document.

- Process PDFs: After uploading the PDF, click "Process PDFs" to extract the text and create the vector embeddings.

- Ask a Question: Once the document has been processed, enter a question in the "Question" text input box. The system will return the most relevant answer from the uploaded document.

# Project Structure

- main.py: The main Streamlit application script.
- vector_index.faiss: A faiss file to store the FAISS index.
- .env: Configuration file for storing your OpenAI API key.
