from deep_translator import GoogleTranslator


def smart_translate(text, target="en", mode="chat"):
    """
    mode:
    - formal = normal translation
    - chat = WhatsApp style (simple + casual)
    """

    try:
        translated = GoogleTranslator(
            source='auto',
            target=target
        ).translate(text)

        if mode == "chat":
            return make_chat_style(translated)

        return translated

    except:
        return "Translation failed"


def make_chat_style(text):
    """
    Converts formal text into WhatsApp style (simple learning mode)
    """

    rules = {
        "I am": "I'm",
        "I will": "I'll",
        "do not": "don't",
        "cannot": "can't",
        "going to": "gonna",
        "want to": "wanna",
        "because": "coz",
        "you are": "you're",
        "please": "pls"
    }

    result = text

    for k, v in rules.items():
        result = result.replace(k, v)

    return result
