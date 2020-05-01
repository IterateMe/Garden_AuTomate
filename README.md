# Garden_AuTomate
This repo is dedicated to the iterative implementation of my own garden irrigation automation system. Feel free to add and comment!
I personnaly used a drop by drop irrigation system because it is probably the most efficient and low profile but not the least expensive, but it can be used with any other tool.
There is no predefined irrigation time or schedule, you will have to define it by your own means and needs.
(Further updates will include links to weather stations and moisture sensors)

This project has been succesfully tested on "Rpi 3B+" & "Rpi Zero WH" with the Raspbian OS (Desktop & Lite versions)


Notes:
- First, you have to make sure you have the latest version of python-crontab library installed with "pip" on your RPi. (the ubuntu repository you access with "sudo apt-get install python-crontab" is not up to date)
          pip install python-crontab
          (if pip isn't recognised, install it with "sudo apt-get install pip")

- In order to run the scripts properly, do so from the command prompt as it is the most reliable way to run scripts on a Rpi.

Content description:
- app.py is the main script from witch you can manually turn on and off the solenoid valve and power of your RPi headless if you need to securelly power it off.
    You can also add as much solenoid valve as you want to app.py, instanciating them from the API.

<!--- run.py is the script the cron deamon runs for each schedule set in the crontab. If you want to test it individually, make sure you start app.py as they are built to work together.
    Also, when run it in the command prompt, make sure to add a time argument for the number of seconds you want it to run.
    For exemple, if you want to test it for 15 seconds, type: "python run.py 15"
    This script also include the "pause" while run.py runs. (blinking led)--->

<!--- pycron.py is the script used to enter your irrigation schedules into crontab.
    If you want to remove all your crontab lines, type "crontab -r" from the command prompt.--->

- API.py contains all the class and methods used in the other scripts.
