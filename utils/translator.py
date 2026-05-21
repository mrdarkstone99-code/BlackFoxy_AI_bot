from deep_translator import GoogleTranslator

def translate_text(text, target="en"):
    try:
        translated = GoogleTranslator(
            source='auto',
            target=target
        ).translate(text)

        return translated

    except Exception:
        return "Translation failed"
