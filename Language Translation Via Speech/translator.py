from googletrans import Translator

translator = Translator()

def translate_text(text, dest_language="fr"):
    try:
        result = translator.translate(text, dest=dest_language)
        print(f"🌍 Translated: {result.text}")
        return result.text
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return None
