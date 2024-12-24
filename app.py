import os
import io
import streamlit as st
import pickle
import time
import langchain
from PyPDF2 import PdfReader
from langchain_openai import OpenAI
from langchain.schema import Document
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Streamlit app
st.title("Interactive QA System")
st.sidebar.title("Upload Question Paper")

# File upload for vector store
uploaded_file = st.sidebar.file_uploader("Upload Question Paper", type="pdf")



process_pdf_clicked = st.sidebar.button("Process PDFs")
file_path = "vector_index.faiss"



# Initialize OpenAI model
main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)



if process_pdf_clicked:
    # load data
    # loader = UnstructuredPDFLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    # data = loader.load()

    if uploaded_file is not None:
        main_placeholder.text("Data Loading...Started...✅✅✅")
        pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
        pdf_text = ""
        
        # Extract text from all pages
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

        document = Document(page_content=pdf_text, metadata={"source": uploaded_file.name})

        # split data
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        main_placeholder.text("Text Splitter...Started...✅✅✅")
        docs = text_splitter.split_documents([document])
        # st.write(docs[0])
        # st.write(docs[1])
        # st.write(docs[2])


        # create embeddings and save it to FAISS index

        embeddings = OpenAIEmbeddings()
        vectorindex_openai = FAISS.from_documents(docs, embeddings)
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        time.sleep(2)

        vectorindex_openai.save_local(file_path)





query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(file_path, embeddings,allow_dangerous_deserialization = True)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
        # result will be a dictionary of this format --> {"answer": "", "sources": [] }
        st.header("Required Questions:")
        st.write(result["answer"])
