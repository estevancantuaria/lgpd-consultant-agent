from typing import Any, Dict
from graph.state import GraphState
from graph.chains.scope_verification import scope_verification_chain

def verify_scope(state: GraphState) -> Dict[str, Any]:
    """
    Verifica se a pergunta está dentro do escopo da LGPD.
    
    Args:
        state (GraphState): Estado atual do grafo
        
    Returns:
        Dict[str, Any]: Estado atualizado com a verificação de escopo
    """
    print("---VERIFY SCOPE---")
    question = state["question"]
    
    result = scope_verification_chain.invoke({"question": question})
    is_within_scope = result.strip().lower() == "true"
    
    if not is_within_scope:
        return {
            "is_within_scope": False,
            "generation": "Desculpe, mas esta pergunta está fora do escopo da LGPD.",
            "question": question
        }
    
    return {
        "is_within_scope": True,
        "question": question
    } 