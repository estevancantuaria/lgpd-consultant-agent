from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "Me faça um resumo dos pontos mais importantes da lei geral de proteção de dados?"}))
