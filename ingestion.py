from dotenv import load_dotenv

load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def ingest_docs():

    loader = PyPDFLoader("lgpd.pdf", extract_images=False)
    raw_documents = loader.load_and_split()
     
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
    
    db = Chroma.from_documents(
        documents=documents,
        collection_name="lgpd",
        embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
        persist_directory="./chroma_db"
    )
    
    print("Finish")

if __name__ == "__main__":
    ingest_docs()