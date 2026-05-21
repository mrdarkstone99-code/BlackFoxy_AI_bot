import random

def generate_reply(text: str):
    text = text.lower()

    # Basic intelligence layer (upgradeable later)
    if "hello" in text:
        return "Hello 👋 I am BlackFoxy AI. Ready to assist you."

    if "help" in text:
        return "I can chat, translate, and solve basic problems. Send anything."

    if "code" in text:
        return "Send your code problem. I will explain it step by step."

    if "what can you do" in text:
        return "I can chat, translate languages, and assist with coding logic."

    # Smart fallback (feels AI-like, not empty)
    responses = [
        "I am thinking about your message...",
        "Interesting 🤔 tell me more.",
        "Can you explain it differently?",
        "I understand. Continue..."
    ]

    return random.choice(responses)
