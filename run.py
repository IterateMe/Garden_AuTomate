import time

import RPi.GPIO as GPIO
from sys import argv as arg

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup([16,15,13], GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

duration = int(arg[1])
status = [1]

def on():
    global duration
    global status
    print("ON", bool(status), duration)
    GPIO.output([16,15], 1)
    if duration >= 0 and bool(status):
        time.sleep(1)
        duration -= 1

def pause():
    global duration
    global status
    print("PAUSE", bool(status), duration)
    GPIO.output([16,15], 0)
    blink(0.5)

def off():
    GPIO.output([16,15], 0)
    print("OFF")

def blink(speed):
    GPIO.output(15, 1)
    time.sleep(speed)
    GPIO.output(15, 0)
    time.sleep(speed)

def callback(self):
    global status
    if bool(status):
        status.remove(1)
    else:
        status.append(1)


if __name__ == "__main__":
    GPIO.add_event_detect(18, GPIO.RISING, callback = callback, bouncetime=400)
    try:
        while duration >= 0:
            if bool(status):
                on()
            else:
                pause()
        off()
        if not GPIO.input(13):
            print("Cleanup")
            GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
