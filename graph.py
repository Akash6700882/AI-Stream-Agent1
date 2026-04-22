from langgraph.graph import StateGraph, END
from typing import TypedDict

from intent import detect_intent
from rag import rag_node
from tools import tool_node
from llm import safe_gemini_call


class AgentState(TypedDict):
    user_input: str
    intent: str
    response: str
    name: str
    stage: str


# =========================
# INTENT NODE
# =========================
def intent_node(state):
    if state.get("stage") == "asking_name":
        return state

    intent = detect_intent(state["user_input"])

    return {**state, "intent": intent}


# =========================
# ROUTER
# =========================
def router(state):

    if state.get("stage") == "asking_name":
        return "capture_name"

    if state["intent"] == "pricing":
        return "rag"

    elif state["intent"] == "buy":
        return "ask_name"

    elif state["intent"] == "greeting":
        return "respond"

    else:
        return "rag"


# =========================
# GREETING
# =========================
def respond_node(state):
    return {
        **state,
        "response": "Hello! How can I help you today?"
    }


# =========================
# ASK NAME
# =========================
def ask_name_node(state):

    prompt = "Ask the user for their name politely in one short sentence."

    response = safe_gemini_call(prompt) or "May I know your name?"

    return {
        **state,
        "response": response,
        "stage": "asking_name"
    }


# =========================
# CAPTURE NAME
# =========================
def capture_name_node(state):

    name = state["user_input"]

    tool_node({"name": name})

    return {
        **state,
        "name": name,
        "stage": "done",
        "response": f"Thanks {name}! Our team will contact you."
    }


# =========================
# BUILD GRAPH
# =========================
builder = StateGraph(AgentState)

builder.add_node("intent", intent_node)
builder.add_node("rag", rag_node)
builder.add_node("respond", respond_node)
builder.add_node("ask_name", ask_name_node)
builder.add_node("capture_name", capture_name_node)

builder.set_entry_point("intent")

builder.add_conditional_edges(
    "intent",
    router,
    {
        "rag": "rag",
        "respond": "respond",
        "ask_name": "ask_name",
        "capture_name": "capture_name"
    }
)

builder.add_edge("rag", END)
builder.add_edge("respond", END)
builder.add_edge("ask_name", END)
builder.add_edge("capture_name", END)

graph = builder.compile()