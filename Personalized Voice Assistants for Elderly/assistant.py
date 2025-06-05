import json
import datetime
from speech_io import speak

def greet_user(name="Grandma"):
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak(f"Good morning, {name}")
    elif hour < 18:
        speak(f"Good afternoon, {name}")
    else:
        speak(f"Good evening, {name}")

def load_reminders():
    try:
        with open("reminders.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def check_reminders():
    now = datetime.datetime.now().strftime("%H:%M")
    reminders = load_reminders()
    for reminder in reminders:
        if reminder["time"] == now:
            speak(f"Reminder: {reminder['message']}")

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def get_date():
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {today}")

def handle_command(command):
    if "time" in command:
        get_time()
    elif "date" in command:
        get_date()
    elif "reminder" in command:
        check_reminders()
    elif "stop" in command or "goodbye" in command:
        speak("Goodbye! Take care.")
        return False
    else:
        speak("Sorry, I don't know how to do that yet.")
    return True
