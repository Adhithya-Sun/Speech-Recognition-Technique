from speech_io import listen, speak
from assistant import greet_user, handle_command, check_reminders
import time

def main():
    speak("Voice assistant is starting...")
    greet_user("Grandma")

    while True:
        check_reminders()
        command = listen()
        if command:
            if not handle_command(command):
                break
        time.sleep(3)  # avoid constant loop polling

if __name__ == "__main__":
    main()
