from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

system = """Você é um especialista em LGPD (Lei Geral de Proteção de Dados) e deve avaliar se a pergunta está dentro do escopo da lei.

Regras para determinar se está no escopo:
- A pergunta deve estar relacionada à proteção de dados pessoais
- Deve envolver aspectos como privacidade, tratamento de dados, direitos dos titulares, etc.
- Questões técnicas de TI que não envolvam dados pessoais estão fora do escopo
- Questões gerais de negócios sem relação com dados pessoais estão fora do escopo

Responda apenas 'true' se estiver no escopo ou 'false' se estiver fora do escopo."""

scope_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Pergunta: {question}")
    ]
)

scope_verification_chain = scope_prompt | llm | StrOutputParser() 