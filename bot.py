import random
import re
import json
import os
from datetime import datetime

# -----------------------------------------------------------------
# 💾 OFFLINE MEMORY ENGINE (Permanent Local JSON Storage)
# -----------------------------------------------------------------
MEMORY_FILE = "ai_brain_memory.json"

def load_memory() -> dict:
    """Loads the permanent user data from the local storage file."""
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            # Fallback if file gets corrupted
            pass
            
    # Default memory state if starting fresh
    return {
        "user_name": None,
        "notes": {},
        "chat_count": 0,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

def save_memory(memory_data: dict):
    """Saves the memory state permanently back to your hard drive."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory_data, file, indent=4, ensure_ascii=False)


# -----------------------------------------------------------------
# 🧠 MAIN PROCESSING UNIT
# -----------------------------------------------------------------
def generate_reply(text: str, memory: dict) -> str:
    # Update total structural interaction count
    memory["chat_count"] += 1
    save_memory(memory)

    # Clean text input
    original_input = text.strip()
    text = text.lower().strip()
    
    # Quick access to user name strings
    name = memory["user_name"] if memory["user_name"] else "bro"

    # --- SETUP / CHANGE NAME MECHANIC ---
    if "my name is " in text:
        # Extract everything after "my name is "
        new_name = original_input[text.find("my name is ") + 11:].strip()
        if new_name:
            memory["user_name"] = new_name
            save_memory(memory)
            return f"🤝 System updated! From now on, I will call you **{new_name}** forever."
        return "I didn't catch the name. Type: *my name is [your name]*"

    if "what is my name" in text or "who am i" in text:
        if memory["user_name"]:
            return f"😎 You are **{memory['user_name']}**. I have it locked in my offline data drive!"
        return "You haven't told me your name yet! Tell me by typing: *my name is [your name]*"

    # --- WHATSAPP STYLE INTERPRETATION LAYER ---
    whatsapp_rules = {
        "i am": "i'm", "you are": "you're", "do not": "don't",
        "cannot": "can't", "going to": "gonna", "want to": "wanna",
        "because": "coz", "please": "pls"
    }
    for k, v in whatsapp_rules.items():
        text = text.replace(k, v)

    # --- GREETINGS ---
    if any(greet in text for greet in ["hi", "hello", "hey"]):
        return random.choice([
            f"Hey {name} 👋 what’s up?",
            f"Hello {name} 😄 I’m completely operational offline.",
            f"Hi {name} 😎 tell me, what are we building?"
        ])

    # --- FEELINGS / STATUS CHECK ---
    if "how are you" in text:
        return random.choice([
            f"I’m good {name} 👍 what about you?",
            "All core scripts running green 😄 you?",
            f"Feeling active ⚡ Ready to clean up code with you, {name}."
        ])

    # --- GOODBYE ---
    if "bye" in text:
        return f"Bye {name} 👋 take care, talk later!"

    # -------------------------------------------------------------
    # 🗃️ OFFLINE UTILITIES: ADVANCED FEATURE ADDITIONS
    # -------------------------------------------------------------
    
    # 📝 Note Pad System (Save drafts, scripts, or lore snippets offline)
    note_save_match = re.search(r"remember\s+(.+?)\s*=\s*(.+)", text)
    if note_save_match:
        key = note_save_match.group(1).strip()
        val = original_input[re.search(r"=", original_input).start() + 1:].strip()
        memory["notes"][key] = val
        save_memory(memory)
        return f"📝 Saved to local memory! Next time you ask for '{key}', I'll print it out."

    if text.startswith("get note "):
        key = text.replace("get note ", "").strip()
        if key in memory["notes"]:
            return f"📋 **Offline Note [{key}]:**\n{memory['notes'][key]}"
        return f"❌ No note found for '{key}'. Save one using: *remember [topic] = [text]*"

    # ⏱️ System Status Check
    if "system status" in text or "brain info" in text:
        return (
            f"⚙️ **Brain Diagnostic Readout:**\n"
            f"▪️ User Registry: {memory['user_name'] if memory['user_name'] else 'Not Registered'}\n"
            f"▪️ Total Interactions: {memory['chat_count']}\n"
            f"▪️ Local Database Status: Connected ✅\n"
            f"▪️ Saved Offline Notes: {len(memory['notes'])} entries"
        )

    # -------------------------------------------------------------
    # 💻 CODING HELP MODE
    # -------------------------------------------------------------
    if any(word in text for word in ["error", "bug", "debug"]):
        return (
            "💻 **Coding Help Mode Active:**\n"
            "1. Double-check your trailing colons (`:`) and structural indentation.\n"
            "2. Ensure variables match cases perfectly.\n"
            "👉 Drop your raw code block or error traceback message right here, and I'll debug it."
        )

    if any(word in text for word in ["python", "code", "script"]):
        return (
            "💻 **Coding Assistant Core:**\n"
            "I parse Python basics, architecture, layout mathematical grids, and string processing.\n"
            "Send your target logic goals!"
        )

    # -------------------------------------------------------------
    # 🗮️ MATH ENGINE (Crash Proof)
    # -------------------------------------------------------------
    math_match = re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", text)
    if math_match:
        a = int(math_match.group(1))
        op = math_match.group(2)
        b = int(math_match.group(3))

        if op == "+": return f"🧮 Answer: {a + b}"
        if op == "-": return f"🧮 Answer: {a - b}"
        if op == "*": return f"🧮 Answer: {a * b}"
        if op == "/":
            if b == 0:
                return "🧮 Answer Error: Division by zero calculation aborted! ❌"
            return f"🧮 Answer: {a / b}"

    # -------------------------------------------------------------
    # 📚 LANGUAGE LEARNING UNIT
    # -------------------------------------------------------------
    if "meaning" in text:
        return "📚 Send me the word, I'll strip away complex jargon and explain it simply."

    if "english" in text:
        return "📚 Language Unit: Ready. We can evaluate sentence layouts or structural grammar offline."

    # -------------------------------------------------------------
    # 🔄 FALLBACK INTERACTION COMPONENT
    # -------------------------------------------------------------
    return random.choice([
        f"hmm 🤔 interesting point...",
        f"okay 👍 let's see where that goes. What's next on the agenda?",
        f"I track exactly what you mean, {name}.",
        "Tell me more details about that 👀",
        f"Interesting... ⚡ Keep processing that thought, {name}."
    ])


# -----------------------------------------------------------------
# 🏃 TERMINAL RUNTIME LOOP
# -----------------------------------------------------------------
if __name__ == "__main__":
    # Boot offline memory engine
    local_memory = load_memory()
    
    print("====================================================")
    print("🧠 OFFLINE AI BRAIN ENGINE STARTED")
    print("====================================================")
    
    # First-time user registry setup
    if not local_memory["user_name"]:
        print("AI: Hello! 🤖 I am running entirely offline on your local computer storage.")
        print("AI: Since my data records are blank, what is your name?")
        initial_name = input("You (enter your name): ").strip()
        if initial_name:
            local_memory["user_name"] = initial_name
            save_memory(local_memory)
            print(f"AI: Perfect! I have stored your profile. Welcome, {initial_name}! ✨")
    else:
        print(f"AI: System online. Welcome back, {local_memory['user_name']}! ⚡")
        print("AI: Type 'system status' to see data stats, or 'bye' to exit safely.")
    print("====================================================\n")

    while True:
        try:
            user_input = input(f"{local_memory['user_name'] if local_memory['user_name'] else 'You'}: ")
            if not user_input.strip():
                continue
                
            reply = generate_reply(user_input, local_memory)
            print(f"AI: {reply}\n")
            
            if "bye" in user_input.lower():
                break
        except (KeyboardInterrupt, SystemExit):
            print("\nAI: Powering down local core threads. Goodbye!")
            break
