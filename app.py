import time

import RPi.GPIO as GPIO
import API

water_valve = API.EValve(16,15,12)
on_led = API.Led(13)
off_button = API.Button(11, 13)

off_button.set_detection(off_button.close_RPi)

on_led.on()

def run():
    time.sleep(60)

if __name__ == "__main__":
    try:
        while True:
            run()
    except KeyboardInterrupt:
        GPIO.cleanup()
