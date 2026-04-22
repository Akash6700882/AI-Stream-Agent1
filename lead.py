def lead_node(state):
    if not state.get("name"):
        return {**state, "response": "What's your name?"}

    if not state.get("email"):
        return {**state, "response": "Your email?"}

    if not state.get("platform"):
        return {**state, "response": "Which platform? (YouTube/Instagram)"}

    # final step
    mock_lead_capture(state["name"], state["email"], state["platform"])

    return {**state, "response": " Lead captured successfully!"}