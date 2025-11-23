from src.chatbot_oop import KnowledgeBase, ChatSession, Bot
import os
import json

# Ensure data folder
os.makedirs("data/sessions", exist_ok=True)

# Load KB from seed
kb_path = os.path.join("data", "kb_seed.json")
kb = KnowledgeBase.load(kb_path)

# Create or load session
session = ChatSession()  # new session
# Optionally try to load an existing session by id (not used here)

bot = Bot(kb, session)

print("=== ChatbotOOP ===")
print("Type 'exit' or 'quit' to save & exit.")
print("Try: 'what is a budget'  or 'mood:happy'")

try:
    while True:
        user = input("\nYou: ").strip()
        if user.lower() in ("exit", "quit"):
            bot.save_state()
            print("Bot: Session saved. Bye!")
            break

        reply, conf = bot.reply(user)
        print(f"Bot: {reply}  [confidence={conf}]")

except KeyboardInterrupt:
    print("\nInterrupted — saving & exiting.")
    bot.save_state()
