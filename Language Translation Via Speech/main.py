from speech_io import listen, speak_gtts
from translator import translate_text

TARGET_LANGUAGE = "fr"  # Change to any ISO 639-1 code (e.g., 'es' for Spanish, 'de' for German)

def main():
    print("🧠 Speech Translator Activated")
    speak_gtts("Please say something to translate", "en")
    
    while True:
        spoken_text = listen()
        if spoken_text:
            translated = translate_text(spoken_text, TARGET_LANGUAGE)
            if translated:
                speak_gtts(translated, TARGET_LANGUAGE)

if __name__ == "__main__":
    main()
