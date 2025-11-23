#!/usr/bin/env python3
"""
budget_chatgpt.py
Simple CLI chatbot with:
- 10 hardcoded QnA (basic budget-related)
- "hi" triggers random replies (if-else based)
- emotion-based replies (happy/sad/angry)
- chat logging to a file with try-except
- uses lists, dicts, loops, functions
"""

import random
import time
import os

# ---------- Hardcoded QnA (10 pairs) ----------
# Stored as a list of tuples so we can iterate with for-loops (and still use if-else control flow).
QNA = [
    ("what is a budget", "A budget is a plan for your income and expenses over a period."),
    ("how to start saving", "Start by tracking expenses for a month, set a small savings goal, automate transfers."),
    ("emergency fund", "Aim for 3-6 months of expenses saved in a liquid account."),
    ("debt repayment tip", "Pay more than the minimum and target highest-interest debts first."),
    ("best savings account", "Look for high-interest savings or fixed deposits depending on your needs."),
    ("should i invest", "Invest if you have an emergency fund and can stay invested for years."),
    ("50 30 20 rule", "50% needs, 30% wants, 20% savings/investments."),
    ("how to track expenses", "Use a simple spreadsheet or an expense tracking app and update daily."),
    ("small monthly budget", "Prioritize essentials, cut subscriptions, cook at home, and set a fixed saving."),
    ("apps for budgeting", "Try Google Sheets, Mint, or any local expense tracker app.")
]

# ---------- Random replies for greetings ----------
GREETING_REPLIES = [
    "Hey! Kaise ho? Main Budget-Bot hoon. Kya help chahiye?",
    "Hello! Batao, aaj paisa save karne ka plan hai kya?",
    "Hi! Ready to tame your money? 💪",
    "Yo! Pooch kuch bhi budgeting ke bare mein."
]

# ---------- Emotion replies ----------
EMOTION_REPLIES = {
    "happy": ["Great to hear! Celebrate small wins — treat yourself smartly.", "Awesome! Good mood = good decisions."],
    "sad": ["Sorry to hear that. Small money wins can lift mood — try saving ₹100 this week.", "It's okay — start tiny and build momentum."],
    "angry": ["Take a breath. Money stress is common — let's make one tiny step forward.", "Anger is valid. Let's set one simple financial goal."]
}

LOGFILE = "budget_chat_log.txt"

# ---------- Utility functions ----------
def save_chat_log(user_input, bot_reply):
    """Append chat exchange to a log file. Uses try-except for safe file handling."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} | USER: {user_input} | BOT: {bot_reply}\n"
    try:
        with open(LOGFILE, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception as e:
        # If logging fails, print a small message but keep bot running
        print("[Warning] Could not write to log file:", e)

def detect_emotion(text):
    """Naive emotion detection by keyword matching. Returns 'happy', 'sad', 'angry', or None."""
    t = text.lower()
    if any(word in t for word in ("happy", "glad", "great", "good", "awesome")):
        return "happy"
    if any(word in t for word in ("sad", "unhappy", "depress", "down", "lonely")):
        return "sad"
    if any(word in t for word in ("angry", "mad", "pissed", "furious")):
        return "angry"
    return None

def find_qna_answer(user_input):
    """
    Look for an answer in the QNA list. This function uses an explicit if-elif-else control flow
    for the important case 'hi', and then a loop + simple matching for QnA pairs.
    """
    ui = user_input.strip().lower()

    # ---------- If-else based handling for greetings ----------
    if ui == "hi" or ui == "hello":
        # pick a random greeting reply
        reply = random.choice(GREETING_REPLIES)
        return reply

    # emotion check using function
    emotion = detect_emotion(ui)
    if emotion:
        # if-else based emotion reply (one branch for each emotion)
        if emotion == "happy":
            return random.choice(EMOTION_REPLIES["happy"])
        elif emotion == "sad":
            return random.choice(EMOTION_REPLIES["sad"])
        elif emotion == "angry":
            return random.choice(EMOTION_REPLIES["angry"])

    # ---------- If-else fallback: exact or keyword match for QnA ----------
    # Try exact matches first
    for question, answer in QNA:
        if ui == question:
            return answer

    # Try keyword matching: check if any important keyword from the question appears in user input
    # This loop is explicit and uses if-else inside for clarity
    for question, answer in QNA:
        keywords = question.split()  # naive keywords from question phrase
        for kw in keywords:
            if kw in ui:
                # small heuristic: if user input contains any keyword, return answer
                return answer

    # Fallback default replies (if-else based)
    if "budget" in ui:
        return "Budget bananas ka simple step: (1) Income note karo (2) Fixed kharch list karo (3) Save set karo."
    elif "save" in ui or "saving" in ui:
        return "Start small: ₹500 per month — automate it."
    elif "exit" in ui or ui == "quit":
        return "exit"  # sentinel to tell main loop to stop
    else:
        return "Hmm, samajh nahi aaya. Thoda simple shabd mein try karo (e.g., 'what is a budget')."

# ---------- Main CLI loop ----------
def main():
    print("==== Budget ChatGPT (hardcoded mini-bot) ====")
    print("Type 'exit' or 'quit' to leave.")
    try:
        while True:
            user_input = input("\nYou: ").strip()
            if not user_input:
                print("Bot: Please type something (or 'exit' to quit).")
                continue

            reply = find_qna_answer(user_input)
            # If user requested exit via matching
            if reply == "exit":
                print("Bot: Bye! Good luck with your budgeting. 👋")
                save_chat_log(user_input, "User exit")
                break

            print("Bot:", reply)
            save_chat_log(user_input, reply)

    except KeyboardInterrupt:
        print("\n[Interrupted] Exiting. Bye!")
    except Exception as e:
        # top-level try-except to show errors but keep message human
        print("[Error] Something went wrong:", e)

if __name__ == "__main__":
    main()
