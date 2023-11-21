import datetime
import time
from tkinter import *

def alarm(set_alarm_timer):
    while True:
        #waits for 1 sec before moving onto next step
        time.sleep(1)
        #finds the current time and date and sets it to current_time variable
        current_time = datetime.datetime.now()
        #sets current_time time to H:M:S format, storing it in now variable
        now = current_time.strftime("%H:%M:%S")
        #sets current_time date to D:M:Y format, storing it in date
        date = current_time.strftime("%d:%m:%Y") 

        #prints out the current date and time
        print("Date: " + date + " Time: " + now)

        if now == set_alarm_timer:
            tkinter.messagebox.showwarning(title="warning",message="Time is Up")
        break

