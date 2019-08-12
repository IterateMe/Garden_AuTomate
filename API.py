import time
import subprocess

import RPi.GPIO as GPIO



class EValve:
    def __init__(self, pin_relay, pin_led, pin_button):
        self.pin_relay = pin_relay
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_relay, GPIO.OUT)
        
        self.led = Led(pin_led)
        self.button = Button(pin_button)
        GPIO.add_event_detect(pin_button, GPIO.RISING, callback = self.manual, bouncetime = 1000)
        
    def on(self):
        print("EValve {} ON".format(self.pin_relay))
        GPIO.output(self.pin_relay, 1)
        self.led.on()
        
    def off(self):
        print("EValve {} OFF".format(self.pin_relay))
        GPIO.output(self.pin_relay, 0)
        self.led.off()
        
    def manual(self, *args):
        if GPIO.input(self.pin_relay):
            self.off()
        else:
            self.on()

    def scheduled(self, duration, *args):
        duration = duration
        self.on()
        time.sleep(duration*60)
        self.off()




class Led:
    def __init__(self, pin_led):
        self.pin_led = pin_led
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_led, GPIO.OUT)
        
    def on(self):
        GPIO.output(self.pin_led, 1)
        print("led {} ON".format(self.pin_led))
        
    def off(self):
        GPIO.output(self.pin_led, 0)
        print("led {} off".format(self.pin_led))
        
    def manual_led(self):
        if GPIO.input(self.pin_led):
            self.off()
        else:
            self.on()
        
    def blink(self, count=15, sleep=0.1):
        last_until = count
        while last_until != 0:
            self.on()
            time.sleep(sleep)
            self.off()
            time.sleep(sleep)
            last_until -= 1


class Button:
    def __init__(self, pin_button, pin_led=None):
        self.pin_button = pin_button
        self.pin_led = pin_led
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_button, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
        if self.pin_led != None:
            GPIO.setup(pin_led, GPIO.OUT)
            self.led = Led(pin_led)
        
    def set_detection(self, callback):
        GPIO.add_event_detect(self.pin_button, GPIO.RISING, callback=callback, bouncetime = 1000)
        
    def close_RPi(self, *args):
        self.led.blink(count=10)
        if GPIO.input(self.pin_button):
            GPIO.cleanup()
            subprocess.call("sudo shutdown -h now", shell=True)
        else:
            GPIO.output(self.pin_led, 1)
