#  AutoStream AI Agent

>  *An intelligent, state-driven AI sales agent powered by LangGraph + Gemini + RAG*

---

##  Overview

**AutoStream AI Agent** is a next-generation conversational AI system designed to simulate a real-world **sales automation assistant**.

It goes beyond a basic chatbot by introducing:
- 🧠 Multi-step reasoning (state machine flow)
- 🔁 Dynamic intent routing
- 📚 Retrieval-Augmented Generation (RAG)
- 🎯 Lead qualification system
- 🤖 LLM-powered conversational intelligence (Gemini API)

This project demonstrates how modern AI agents are built in production systems.

---

##  What Makes This Special?

Unlike traditional chatbots, this system:

✔ Remembers conversation state  
✔ Routes queries intelligently  
✔ Separates logic into modular nodes  
✔ Uses fallback + LLM hybrid reasoning  
✔ Handles real-world sales funnel logic  

---

##  System Architecture

              ┌──────────────┐
              │  User Input  │
              └──────┬───────┘
                     ↓
         ┌──────────────────────┐
         │ Intent Detection Node │
         └─────────┬────────────┘
                   ↓
    ┌──────────────┼──────────────┐
    ↓              ↓              ↓
    Greeting Node RAG Node Lead Flow Node
     │             │              │
     └──────┬──────┴──────┬──────┘
                  ↓ ↓
       Gemini API Tool Execution
                  ↓
            Final Response




            
---

## ⚙️ Tech Stack

| Layer | Technology |
|------|------------|
|  LLM | Google Gemini API |
|  Orchestration | LangGraph |
|  Knowledge System | RAG (Retrieval-Augmented Generation) |
|  Backend | Python |
|  Config | dotenv |
|  Tools | Custom Tool Nodes |

---

##  Core Features

###  1. Intent Detection Engine
- Classifies user input into:
  - Greeting
  - Pricing
  - Buy Intent
  - Unknown (LLM fallback)

---

### 📚 2. RAG Pipeline
- Stores structured business knowledge:
  - Pricing plans
  - Policies
- Ensures **fast + accurate responses**
- Avoids hallucination from LLM

---

###  3. Gemini-Powered Responses
- Generates natural human-like replies
- Handles dynamic conversation:
  - Asking user name
  - Sales interaction flow

---

###  4. Lead Generation System
- Detects high-intent users
- Collects:
  - Name
  - Email (extendable)
  - Platform (future scope)
- Stores via tool node simulation

---

###  5. LangGraph State Engine
- Maintains conversation state:
```python
state = {
  "user_input": "",
  "intent": "",
  "stage": "",
  "name": ""
}
User: hi
Agent: Hello! How can I help you today?
User: price
Agent: 
Basic Plan: $29/month
Pro Plan: $79/month
User: I want to buy
Agent: May I know your name?
User: Aakash
Agent: Thanks Aakash! Our team will contact you soon.

🧩 Project Flow (Real World Mapping)

This system mimics real SaaS sales pipelines:

Visitor → Chat → Interest Detection → Qualification → Lead Capture → CRM Entry


👨‍💻 Author

Aakash
EEE - IIT Guwahati | AI Systems Builder
Focused on: AI Agents, LLM Apps, ML Systems
