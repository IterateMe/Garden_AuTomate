import time

from flask import Flask, g, render_template, flash, redirect, url_for, request

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import RPi.GPIO as GPIO

from API import EValve, Button, Led

water_valve = EValve(16,15,12)
on_led = Led(13)
off_button = Button(11, 13)

off_button.set_detection(off_button.close_RPi)

on_led.on()

sched = BackgroundScheduler()
sched.start()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def main():
    sched.print_jobs()
    return render_template('main.html', EValve_status = GPIO.input(16), app_status = GPIO.input(13), jobs = sched.print_jobs())

@app.route('/Manual')
def pushed_button():
    water_valve.manual()
    return redirect(url_for('main'))

@app.route("/scheduler", methods=["GET","POST"])
def schedule():
    return render_template("form.html", jobs = sched.print_jobs())

@app.route("/form_handler", methods=["GET","POST"])
def handling():
    hour = str(request.form["hour"])
    min = str(request.form["min"])
    duration = int(request.form["duration"])
    sched.add_job(water_valve.scheduled, CronTrigger.from_crontab("{} {} * * *".format(min, hour)), [duration])
    return redirect(url_for("schedule"))

if __name__ == "__main__":
    app.debug(False)