from voice_control import listen_command, speak
from appliance_controller import control_appliance

def process_command(command):
    if command:
        if "turn on" in command:
            if "light" in command:
                control_appliance("light", "on")
                speak("Turning on the light.")
            elif "fan" in command:
                control_appliance("fan", "on")
                speak("Turning on the fan.")
        elif "turn off" in command:
            if "light" in command:
                control_appliance("light", "off")
                speak("Turning off the light.")
            elif "fan" in command:
                control_appliance("fan", "off")
                speak("Turning off the fan.")
        else:
            speak("Command not recognized.")
    else:
        speak("Please repeat your command.")

if __name__ == "__main__":
    speak("Voice controlled system activated.")
    while True:
        command = listen_command()
        process_command(command)
