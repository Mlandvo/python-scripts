from tkinter import *
import alarmscript as alarm

#initializes Tkinter
clock = Tk()

#window title and size
clock.title("Alarm Clock")
clock.geometry("400x200")

#Labels for UI experience
time_format = Label(clock,text="Enter time in 24hr forrmat",fg="red",bg="black",font ="Arial").place(x=60,y=120)
addTime = Label(clock,text="Hour  Min    Sec",font=60).place(x=110)
setYourAlarm = Label(clock,text="When to awaken",fg="blue",relief="solid",font=("Helevetica",7,"bold")).place(x=0,y=29)

#hour,min,sec variables
hour = StringVar()
min = StringVar()
sec = StringVar()

#text input for time
hourTime = Entry(clock,textvariable=hour,bg="pink",width=15).place(x=110,y=30)
minTime = Entry(clock,textvariable=min,bg="pink",width=15).place(x=150,y=30)
secTime = Entry(clock,textvariable=sec,bg="pink",width=15).place(x=200,y=30)

#button to set alarm
def actual_time():
    alarm.set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm.alarm(alarm.set_alarm_timer)

#will call function actual_time() from alarmscript.py
submit = Button(clock,text="Set alarm",fg="red",width=10,command= actual_time).place(x=110,y=70)

clock.mainloop()
