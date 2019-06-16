import time

from flask import Flask, g, render_template, flash, redirect, url_for
import RPi.GPIO as GPIO
from API import EValve, Button, Led

water_valve = EValve(16,15,12)
on_led = Led(13)
off_button = Button(11, 13)

off_button.set_detection(off_button.close_RPi)

on_led.on()

app = Flask(__name__)

@app.route('/')
def main():
    return "app on: {}".format(GPIO.input(13))

if __name__ == "__main__":
    try:
        app.debug(False)
    except KeyboardInterrupt:
        GPIO.cleanup()