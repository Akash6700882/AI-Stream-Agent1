def rag_node(state):
    query = state["user_input"].lower()

    if "price" in query or "plan" in query:
        return {
            **state,
            "response": """Basic Plan: $29/month
Pro Plan: $79/month"""
        }

    return {
        **state,
        "response": "I can help with pricing or purchases."
    }