from ctypes import *
from Tkinter import *
import time

root = Tk()
time1 = ''
clock = Label(root, font=('arial', 20))
clock.pack(fill=BOTH, expand=1)

mylib = CDLL("./libflags.so")

def tick():
    global time1
    mylib.main()
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=mylib.getDistance())
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >;200 ms, but display gets jerky
    clock.after(200, tick)

tick()
root.mainloop(  )
