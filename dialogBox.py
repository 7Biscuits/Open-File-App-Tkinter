import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

crrdir = os.getcwd()
root = tkinter.Tk()

def open():
    global openFile
    global showFile
    root.filename = filedialog.askopenfilename(initialdir=f"{crrdir}", title="Select a File", filetypes=(('png files', '*.png'), ('any files', '*.*'))) # when open button is clicked then the program return its location on the computer
    openFile = ImageTk.PhotoImage(Image.open(root.filename))
    showFile = Label(root, image=openFile).pack()

showFileButton = Button(root, text="Open File", command=open).pack()

root.mainloop()