"""
run_tests.py
Manual unit-style tests for the ChatbotOOP project.
Run: python run_tests.py
"""

from src.chatbot_oop import KnowledgeBase, ChatSession, Bot
import os
import json
import tempfile

# Load seed KB
kb = KnowledgeBase.load(os.path.join("data", "kb_seed.json"))

# Prepare session (use temp folder so it doesn't conflict)
session = ChatSession()
bot = Bot(kb, session)

def test_exact_match():
    q = "what is a budget"
    reply, conf = bot.reply(q)
    assert conf == 0.9, "Exact match should give confidence 0.9"
    print("Test 1 (exact match) passed.")

def test_substring_rephrase():
    q = "Tell me about budgets"  # contains 'budget' substring
    reply, conf = bot.reply(q)
    assert conf == 0.9, "Substring match should hit KB entry"
    print("Test 2 (substring match) passed.")

def test_unrelated():
    q = "who won the world cup 1992"
    reply, conf = bot.reply(q)
    assert conf <= 0.3, "Unrelated should return fallback with low confidence"
    print("Test 3 (unrelated) passed.")

def test_memory_trim_and_save():
    # create 25 turns
    for i in range(25):
        bot.reply(f"user turn {i}")
    # memory should be last 20
    assert len(session.memory) == 20, f"memory len should be 20 but is {len(session.memory)}"
    # save session and check file created
    session.save_session()
    path = session._session_path
    assert os.path.exists(path), "session file should exist after save"
    print("Test 4 (memory trim & save) passed.")

def test_restart_load():
    # save and reload into new session object
    session.save_session()
    new_session = ChatSession(session_id=session.session_id)
    new_session.load_session()
    assert len(new_session.turns_all) >= 25, "Loaded session should have full history"
    print("Test 5 (restart & load) passed.")

if __name__ == "__main__":
    test_exact_match()
    test_substring_rephrase()
    test_unrelated()
    test_memory_trim_and_save()
    test_restart_load()
    print("ALL TESTS PASSED (manual assertions).")
