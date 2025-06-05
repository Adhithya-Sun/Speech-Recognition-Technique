import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import playsound
import os
import uuid

engine = pyttsx3.init()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None
    except sr.RequestError:
        print("❌ Speech recognition service unavailable")
        return None

def speak_offline(text):
    engine.say(text)
    engine.runAndWait()

def speak_gtts(text, lang):
    tts = gTTS(text=text, lang=lang)
    filename = f"temp_{uuid.uuid4()}.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
