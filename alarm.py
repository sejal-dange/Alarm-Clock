from playsound import playsound
from tkinter import *
from PIL import ImageTk, Image
from win10toast import ToastNotifier
import datetime
import time

def alarm(set_alarm):
    toast = ToastNotifier()
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("Alarm Clock")
            toast.show_toast("Time To Wake Upp!!",duration=3)
            playsound("alarmtone.mp3")
            break

def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

root = Tk()
root.title("Alarm Clock")
root.geometry("252x200")
root.minsize(252,200)
root.maxsize(252,200)
HEIGHT = 252
WIDTH = 200

frame=Frame(root,bg="white")
frame.place(relwidth=1,relheight=1)

background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\HP\Desktop\Alarm\alarm.png"))
background_label = Label(frame, image = background_image)
background_label.place(relwidth=1,relheight=1)

info = Label(frame,text = "(24)Hour  Min   Sec").place(relx=0.4,rely=0.1)#50
set_time = Label(frame,text = "Set Time",bg="black",fg="white",font=("Cambria",12,"bold")).place(relx=0.02,rely=0.23)#x=50,30

#Entry Variables
hour = StringVar()
min = StringVar()
sec = StringVar()

#Entry Widget
hour_E = Entry(frame,textvariable = hour,bg="grey", fg="white",width=4,font=("Cambria",10,"bold")).place(relx=0.41,rely=0.24)#60,30
min_E = Entry(frame,textvariable = min,bg="grey", fg="white", width=4,font=("Cambria",10,"bold")).place(relx=0.54,rely=0.24)#90,30
sec_E = Entry(frame,textvariable = sec,bg="grey", fg="white", width=4,font=("Cambria",10,"bold")).place(relx=0.68,rely=0.24)#120,30

submit = Button(frame,text = "Set Alarm",width = 9,bg = "black",fg="white",font=("Cambria",13,"bold"),command = getvalue)
submit.place(relx =0.43,rely=0.53)

root.mainloop()

