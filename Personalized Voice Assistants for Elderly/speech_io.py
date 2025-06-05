import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import uuid
from playsound import playsound

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # slower speech for elderly users

def speak(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        filename = f"temp_{uuid.uuid4()}.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except:
        engine.say(text)
        engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"Recognized: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t understand that.")
        return None
    except sr.RequestError:
        speak("Service is unavailable.")
        return None
