from graph import graph

state = {
    "user_input": "",
    "intent": "",
    "response": "",
    "name": "",
    "stage": "normal"
}

print("Agent Running (type exit to quit)\n")

while True:
    user_input = input("You: ")

    if user_input == "exit":
        break

    state["user_input"] = user_input

    result = graph.invoke(state)

    state = result  # 🔥 MEMORY

    print("Agent:", result["response"])