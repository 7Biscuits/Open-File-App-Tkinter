import tkinter  
from tkinter import *

root = tkinter.Tk()
root.title("Calculator")

user_entry = Entry(root, width=35, borderwidth=5)
user_entry.grid( row=0, column=0, columnspan=3, padx=10, pady=10)

def on_button_click(number):
    current = user_entry.get()
    user_entry.delete(0, END)
    user_entry.insert(0, str(current) + str(number))

def clear():
    user_entry.delete(0, END)

def equal():
    second_num = user_entry.get()
    user_entry.delete(0, END)

    if math == 'addition':
        user_entry.insert(0, f_num + int(second_num))

    elif math == 'substraction':
        user_entry.insert(0, f_num - int(second_num))

    elif math == 'multiplication':
        user_entry.insert(0, f_num * int(second_num))

    elif math == 'division':
        user_entry.insert(0, f_num / int(second_num))
        

def addition():
    first_num = user_entry.get()
    global f_num 
    global math
    math = 'addition'
    f_num = int(first_num)
    user_entry.delete(0, END)

def subtraction():
    first_num = user_entry.get()
    global f_num 
    global math
    math = 'substraction'
    f_num = int(first_num)
    user_entry.delete(0, END)

def multiplication():
    first_num = user_entry.get()
    global f_num 
    global math
    math = 'multiplication'
    f_num = int(first_num)
    user_entry.delete(0, END)

def division():
    first_num = user_entry.get()
    global f_num 
    global math
    math = 'division'
    f_num = int(first_num)
    user_entry.delete(0, END)

button_1 = Button(root, text="1", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, borderwidth=3, command=lambda: on_button_click(0))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

equal_button = Button(root, text="=", padx=91, pady=20, command=equal)
clear_button = Button(root, text="Clear", padx=79, pady=20, command=clear)

equal_button.grid(row=5, column=1, columnspan=2)
clear_button.grid(row=4, column=1, columnspan=2)

add_button = Button(root, text="+", padx=39, pady=20, borderwidth=3, command=addition)
substract_button = Button(root, text="-", padx=42, pady=20, borderwidth=3, command=subtraction)
multiply_button = Button(root, text="*", padx=42, pady=20, borderwidth=3, command=multiplication)
divide_button = Button(root, text="/", padx=42, pady=20, borderwidth=3, command=division)

add_button.grid(row=5, column=0)
substract_button.grid(row=6, column=0)
multiply_button.grid(row=6,column=1)
divide_button.grid(row=6, column=2)

root.mainloop()
