from tkinter import *

root = Tk()

name = Entry(root, width=50, borderwidth=5)
name.pack()

def myClick():
    myLabel = Label(root, text=f"Hey there, {name.get()}").pack()

myButton = Button(root, text="Submit", command=myClick).pack()

root.mainloop()