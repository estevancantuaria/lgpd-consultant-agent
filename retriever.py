from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

retriever = Chroma(
    collection_name="lgpd",
    persist_directory="./chroma_db",
    embedding_function=OpenAIEmbeddings(),
).as_retriever()