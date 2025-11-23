# ✅ DAY 3 — ChatbotOOP (OOP + Persistence + Hybrid Matching)

A clean, modular, object-oriented chatbot system built using Python classes.

### 📁 Project Structure

```bash
DAY3-ChatbotOOP/
├─ src/
│  └─ chatbot_oop.py      # All classes (Bot, KnowledgeBase, ChatSession, Responder)
│
├─ data/
│  ├─ kb_seed.json         # 10 seed Q&A pairs
│  └─ sessions/            # Auto-created folder for session history
│
├─ run_bot.py              # CLI runner for the chatbot
├─ run_tests.py            # Manual unit-style tests
├─ DAY3.md                 # Daily checklist summary
└─ README.md               # (This file)
```
### 🎯 Purpose of the Project

The goal of Day 3 is to master Python OOP by building a mini chatbot framework with:

Multiple interacting classes

Clean responsibilities

Hybrid search (word overlap + fuzzy match)

In-memory + persistent conversation history

Configurable mood responses

Fully testable behavior

This day ensures you understand classes, composition, method design, and file-based persistence.

### 🧱 Core Classes (Concept Summary)
##### 1️⃣ KnowledgeBase

Responsibility: Store Q&A data, load/save JSON, provide intelligent search.

Attributes:
entries → list of {"q": "...", "a": "..."}

✔ Holds all knowledge
✔ Clean IO (read/write JSON)
✔ Returns best match(es)

##### 2️⃣ ChatSession

Responsibility: Track full conversation history, auto-trim memory, and save session files.

Attributes:

turns_all → complete conversation
memory → only last 20 turns
session_id

✔ Autosaves after every 5 turns
✔ Writes JSON: data/sessions/session_<id>.json
✔ Keeps conversation alive across restarts

##### 3️⃣ SimpleResponder

Responsibility: Convert user query → (best reply, confidence)
Uses KnowledgeBase.search()

Returns:
Best match → confidence 0.9
Fallback → 0.2
Empty input → 0.0

Independent logic: can be swapped with advanced models later.

✔ Pure logic, no file handling
✔ Confidence scoring included

##### 4️⃣ Bot

Responsibility: The orchestrator.

Holds:
KnowledgeBase
ChatSession
SimpleResponder

Also:
save_state() → saves KB + session

✔ Central point that connects all components
✔ Works like a real-world chat engine

This gives far more accurate matching than plain substring search.

#### 💬 How the Chatbot Works (Simple Flow)

User types input
Bot.reply() processes mood commands if present
SimpleResponder searches KB using hybrid matching
Best answer returned + confidence score
ChatSession stores the turn

Every 5 turns → autosave

If user types exit → bot saves KB + session and quits
🧪 Testing (run_tests.py)

Five manual unit-style tests verify:
Exact match → correct answer + confidence 0.9
Substring / fuzzy match → best relevant match
Unrelated → fallback response

25 turns → memory trimmed to last 20, while full history saved
Session reload → restores previous conversation

Run tests:
```bash
python run_tests.py

▶️ Run the Chatbot
python run_bot.py
```

Try:
```bash
what is a budget
saving tips
fund saving
mood:happy
mood:sad
budget saving fund
```
##### 📄 Design Notes

Composition > inheritance (everything is composed inside Bot)

Session trimming improves performance

JSON format chosen for readability and simplicity

Search kept flexible but lightweight (no external libraries)

Fallback confidence = 0.2 matches “uncertain” behavior

Mood-map implemented as dictionary for easy extensibility