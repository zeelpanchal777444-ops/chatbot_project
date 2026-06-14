# chatbot_project

# Nexus: Advanced Rule-Based AI Chatbot (The Logic Engine)

Nexus is a production-grade, deterministic rule-based AI chatbot built using Python. It operates on the **IPO (Input-Process-Output)** model, acting as a secure "White Box" logic system. It features advanced user sanitization, dynamic keyword pattern matching, runtime context memory (user name tracking), and integrates live system data like time, date, and day.

---

## 🚀 Key Features

* **Infinite Execution Loop:** Stays alive and interacts continuously until an explicit kill command (`exit`, `quit`, `bye`) is triggered.
* **Input Sanitization Pipeline:** Automatically handles case folding (lowercase conversion) and strips unwanted leading/trailing whitespaces to avoid structural crashes.
* **Efficient Hash Map Lookup:** Rejects the anti-pattern `if-elif` ladder in favor of Python Dictionaries (`{}`), ensuring $O(1)$ constant time lookup complexity.
* **Dynamic Memory & Persona:** Extracts, updates, and remembers the user's name during runtime, shifting the prompt dynamically (e.g., from `[user]` to `[Aman]`).
* **Live System Integration:** Uses Python's built-in `datetime` module to pull and display actual real-time clock data, date, and current day.
* **Intelligent Multi-Response Fallback:** Includes a keyword-based scanner for loose matching and a universal catch-all fallback mechanism to prevent dead-ends.

---

## 📂 Project Structure

The project repository is minimalist and lightweight:

```text
AI_Project_1/
├── chatbot.py      # Core logic engine and application code
└── README.md       # Comprehensive system documentation

💬 Sample Interaction (Live Simulation)

==========================================================
             NEXUS LIVE KNOWLEDGE ENGINE          
   Status: ACTIVE | Features: Live Time & Date Enabled   
   (Type 'exit' or 'quit' to terminate the session)       
==========================================================

user : hello
Nexus : Hello! I am Nexus. What is your name? (Type: my name is [your name])

user : My name is Aman
Nexus : Nice to meet you, Aman! Ask me anything.

Aman : what is the current time?
Nexus : The current time is 05:45 PM.

Aman : Tell me about python language
Nexus : Python is a high-level programming language known for readability. It is used in AI and Web Dev.

Aman : can you cook food for me?
Nexus : I processed your question about 'can you cook food for me?', Aman. While I don't have deep details on this specific phrase, you can ask me about: time, date, day, coding, python, or ai!

Aman : quit

Nexus : Goodbye Aman! Keep learning and growing.
==========================================================
