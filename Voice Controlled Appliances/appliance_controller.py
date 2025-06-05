import RPi.GPIO as GPIO
import time

# Configure GPIO pins
APPLIANCES = {
    "light": 17,
    "fan": 27,
}

GPIO.setmode(GPIO.BCM)
for pin in APPLIANCES.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def control_appliance(appliance, state):
    pin = APPLIANCES.get(appliance)
    if pin is None:
        print(f"No such appliance: {appliance}")
        return
    GPIO.output(pin, GPIO.HIGH if state == "on" else GPIO.LOW)
    print(f"{appliance} turned {state}")
