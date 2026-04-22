from llm import safe_gemini_call

def detect_intent(user_input):
    text = user_input.lower()

    # fast fallback (IMPORTANT)
    if any(x in text for x in ["hi", "hello"]):
        return "greeting"

    if any(x in text for x in ["price", "plan"]):
        return "pricing"

    if any(x in text for x in ["buy", "subscribe", "want"]):
        return "buy"

    # LLM fallback
    prompt = f"""
    Classify intent:
    {user_input}

    Options:
    greeting, pricing, buy, other

    Return only one word.
    """

    result = safe_gemini_call(prompt)

    return result if result else "other"