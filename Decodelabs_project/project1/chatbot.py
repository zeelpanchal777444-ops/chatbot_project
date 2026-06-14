# ==========================================
# ========ADVANCED LOGIC ENGINE WITH PERSONA & DYNAMIC CHATBOT=========


# BOT SETTING & CONFIGARATION

BOT_NAME="Nexus" 
user_name="user"

# BASE KNOWLEDGE BASE (CORE RULE)

SUPPORT_SYSTEM ={
    "hello":f"Hello I am {BOT_NAME}. What is your Name? (Type: my name is [your name])",
    "hi":f"Hi there ! {BOT_NAME} at your services. How can I help you today?",
    "your name":f"My name is {BOT_NAME}, your dedicated AI assistant.",
    "who are you":f"I'm {BOT_NAME}, a smart deterministic logic engine.",
    "how are you": "My systems are running at 100% efficiency. Ready for your questions!",
    "pricing":"Our premium services start from $19/month.",
    "hours":"We can active 24/7 to assist you.",
    "help":"you can chat with me naturally, tell me your name, or ask for pricing/hours. You can ask me about: coding, Python, AI, success, health, earth, career, or study! ",
      
    # 2. Technology & Coding Questions
    "coding": "Coding is telling a computer what to do using languages like Python, JavaScript, or C++. Python is best for beginners!",
    "python": "Python is a high-level programming language known for readability. It is used in AI, Web Development, and Data Science.",
    "ai": "Artificial Intelligence (AI) is the simulation of human intelligence by machines. It includes learning, reasoning, and self-correction.",
    "internet": "The internet is a global network of computers connected together to share information instantly.",  
    
    # 3. Life, Career & Motivation
    "success": "Success comes from consistency, hard work, and learning from your failures every single day.",
    "career": "To build a great career, identify your interests, learn in-demand skills (like AI/Coding), and build real projects.",
    "study": "The best way to study is the Pomodoro technique: Focus for 25 minutes, then take a 5-minute break. Repeat!",
    "time management": "Prioritize your tasks using a to-do list. Do the hardest task first thing in the morning.",
    
    # 4. General Knowledge & Health
    "earth": "Earth is the third planet from the Sun and the only astronomical object known to harbor life.",
    "health": "Good health requires 7-8 hours of sleep, drinking plenty of water, eating green vegetables, and daily exercise.",
    "exercise": "Regular exercise improves brain health, helps manage weight, and strengthens muscles and bones.",
    "food": "Food gives us nutrients and energy. For a healthy mind, avoid junk food and eat fruits, nuts, and proteins.",
    
    # 5. Core Business/Support
    "pricing": "Our premium automated services start from $19/month.",
    "hours": "We are online 24/7/365 to process your logical requests.",
    "help": "You can ask me about: coding, Python, AI, success, health, earth, career, or study!"
    
}

print("-----------------------------------------------------------------")
print(f"    {BOT_NAME.upper()} CORE LOGIC ENGINE ONLINE    ")
print("     Stauts : ACTIVE | Intel : Smart Pattern Matching   ")
print("     (Type 'exit' or 'quit' to close the chat safely)   ")

while True:
    raw_input=input(f"\n{user_name} : ")
    clean_input=raw_input.strip().lower()
    
    if clean_input in ['exit','quit','bye']:
        print(f"\n{BOT_NAME} : Goodbye {user_name} I Have a wonderful day ahead.")
        break
    
    if "my name is " in clean_input:
        user_name=raw_input.split("is")[-1].strip()
        print(f"{BOT_NAME} : Nice to meet you , {user_name} ! How can I assist you today?")
        continue
    
    elif "i am" in clean_input and not clean_input.startswith("who"):
        user_name=raw_input.split("am")[-1].strip()
        print(f"{BOT_NAME} : Awesome ! I will call you {user_name} from now on.")
        continue

    system_response=SUPPORT_SYSTEM.get(clean_input)
    
    if system_response:
        print(f"{BOT_NAME} : {system_response}")
    else:
        if"name" in clean_input:
            print(f"{BOT_NAME} : my name is {BOT_NAME},And you are {user_name} !")
        elif "thank" in clean_input:
            print(f"{BOT_NAME} : you're very Welcome, {user_name} ! Always happy to help.")
        elif "ok" in clean_input or "fine" in clean_input:
            print(f"{BOT_NAME} : Great ! What else would you like to discuss ?")
        else:
            print(f"{BOT_NAME} : Interesting question, {user_name} . I understand you are taking about '{raw_input}' , but my knowledge base is currently locked to core support guidelines. Can we talk about pricing,hours , or your profile ?")
    
print("--------------------------------------------")