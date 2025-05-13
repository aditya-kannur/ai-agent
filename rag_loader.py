import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Load text documents
def load_text_file(filepath):
    loader = TextLoader(filepath)
    return loader.load()

text_docs = load_text_file("sample.txt")  

# Split text into chunks
text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = text_splitter.split_documents(text_docs)

# Create embeddings and FAISS vectorstore 
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding)

# Setup QA chain with Groq LLM 
groq_llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-8b-8192"
)

qa_chain = RetrievalQA.from_chain_type(
    llm=groq_llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# Ask questions
while True:
    query = input("\nAsk something about the text (or type 'exit'): ")
    if query.lower() == 'exit':
        break
    result = qa_chain.invoke({"query": query}) 
    print("\nAnswer:", result["result"])
