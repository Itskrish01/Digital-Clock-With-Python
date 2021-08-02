from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk() 
root.title("Clock") # This will be show on window of your clock



def time():
    string = strftime('%H:%M:%S %p') # Format of time
    lable.config(text=string) 
    lable.after(1000, time)

lable = Label(root, font=("ds-digital", 80), background = "Black", foreground = "black") # Interface of your clock
lable.pack(anchor = "center")

time()

mainloop()
