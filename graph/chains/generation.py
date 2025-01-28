from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-4o")
prompt = hub.pull("rlm/rag-prompt")

# Adicionando instrução para resposta em PT-BR
prompt = prompt + "\nPor favor, responda em português do Brasil."

generation_chain = prompt | llm | StrOutputParser()
