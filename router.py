def route_intent(state):
    intent = state["intent"]

    if intent == "greeting":
        return "end"

    elif intent == "pricing":
        return "rag"

    elif intent == "high_intent":
        return "lead"

    elif intent == "unknown":
        return "rag"

    return "end"


# NEW ROUTER AFTER LEAD
def route_after_lead(state):
    if state.get("name") and state.get("email") and state.get("platform"):
        return "tool"
    else:
        return "lead"