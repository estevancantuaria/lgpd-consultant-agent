from typing import List, TypedDict
class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: A pergunta do usuário
        generation: Resposta gerada
        web_search: Se deve fazer busca na web
        documents: Lista de documentos relevantes
        is_within_scope: Se a pergunta está no escopo da LGPD
    """
    question: str
    generation: str
    web_search: bool
    documents: List[str]
    is_within_scope: bool
