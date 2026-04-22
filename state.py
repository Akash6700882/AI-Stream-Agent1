from typing import TypedDict, Optional

class AgentState(TypedDict):
    user_input: str
    intent: Optional[str]
    response: Optional[str]

    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    
    state = {
    "user_input": "",
    "intent": "",
    "stage": "",   # 🔥 ADD THIS
    "name": None,
    "email": None,
    "platform": None,
    "response": ""
}
    