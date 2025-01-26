from typing import Any, Dict

from graph.state import GraphState
from retriever import retriever


def retrieve1(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}
