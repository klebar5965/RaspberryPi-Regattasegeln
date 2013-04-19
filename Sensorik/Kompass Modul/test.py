# Author: Stefan Probst

# C in Python benutzen:
# gcc -Wall -fPIC -c flags.c
# gcc -shared -Wl,-soname,libflags.so.1 -o libflags.so flags.o

# Python: from ctypes import *
# mylib = CDLL("./liprpi_cmps10.so")

from ctypes import *
from Tkinter import *
import time

root = Tk()
clock = Label(root, font=('arial', 20))
clock.pack(fill=BOTH, expand=1)

mylib = CDLL("./librpi_cmps10.so")

def tick():
    mylib.main()
    
    clock.config(text = mylib.getPitch())
    # calls itself every 200 milliseconds
    # could use >;200 ms, but display gets jerky
    clock.after(200, tick)

tick()
root.mainloop()