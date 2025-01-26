from dotenv import load_dotenv

from langgraph.graph import END, StateGraph

from graph.consts import RETRIEVE, GRADE_DOCUMENTS, GENERATE, WEBSEARCH
from graph.nodes.generate import generate
from graph.nodes.grade_documents import grade_documents
from graph.nodes.retrieve1 import retrieve1
from graph.nodes.web_search import web_search
from graph.nodes.verify_scope import verify_scope
from graph.state import GraphState

load_dotenv()

workflow = StateGraph(GraphState)

# Adicionar todos os nós
workflow.add_node("verify_scope", verify_scope)
workflow.add_node(RETRIEVE, retrieve1)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)

# Definir o ponto de entrada como verify_scope
workflow.set_entry_point("verify_scope")

def decide_to_proceed(state):
    """Decide se deve continuar com o processamento ou encerrar."""
    if state["is_within_scope"]:
        print("---DECISION: QUESTION IN SCOPE---")
        return RETRIEVE
    else:
        print("---DECISION: QUESTION OUT OF SCOPE---")
        return END

# Adicionar arestas condicionais a partir da verificação de escopo
workflow.add_conditional_edges(
    "verify_scope",
    decide_to_proceed,
    {
        RETRIEVE: RETRIEVE,
        END: END,
    },
)

# Adicionar as demais arestas do fluxo normal
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)

def decide_to_generate(state):
    """Decide se deve gerar resposta diretamente ou fazer busca web."""
    print("---ASSESS GRADED DOCUMENTS---")
    if state["web_search"]:
        print("---DECISION: NOT ALL DOCUMENTS ARE RELEVANT, INCLUDE WEB SEARCH---")
        return WEBSEARCH
    else:
        print("---DECISION: GENERATE---")
        return GENERATE

workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    },
)

workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")
