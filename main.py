#!/usr/bin/env python

import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Kemon")
root.geometry("150x150")

path = "resources/icon.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def buildgrid(h,w,f):
    height = h
    width = w
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Spinbox(f, from_=0, to=1, width=1,
                           font=Font(family='Helvetica',
                                     size=20,
                                     weight='bold'))
            b.grid(row=i, column=j, padx=10, pady=10)
        
# Warp Grid

warp = tk.Toplevel()
warp.title("Warp Grid")

buildgrid(5,10,warp)


# Weft Grid

weft = tk.Toplevel()
weft.title("Weft Grid")

buildgrid(10,5,weft)

# Tie-up

tieup = tk.Toplevel()
tieup.title("Tie-up")

buildgrid(5,5,tieup)

# Color Palette

# Menu


root.mainloop()


#from tkinter.colorchooser import *
#def getColor():
#    color = askcolor() 
#    print color
#Button(text='Select Color', command=getColor).pack()
