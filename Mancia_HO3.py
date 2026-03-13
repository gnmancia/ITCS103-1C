from tkinter import *

def add():
    result = int(num1.get()) + int(num2.get())
    label_result.config(text=f"The sum is of {num1.get()} + {num2.get()} is {result}.")

def subtract():
    result = int(num1.get()) - int(num2.get())
    label_result.config(text=f"The subtraction of {num1.get()} - {num2.get()} is {result}.")

def multiply():
    result = int(num1.get()) * int(num2.get())
    label_result.config(text=f"The multiplication of {num1.get()} * {num2.get()} is {result}.")

def divide():
    result = int(num1.get()) / int(num2.get())
    label_result.config(text=f"The division of {num1.get()} / {num2.get()} is {result}.")

window = Tk()
window.title("Hi Mancia, Simple Calculator")
window.geometry("205x205")   

label_result = Label(window, text="The sum is of 15 + 20 is 35.")
label_result.pack(pady=5)

frame = Frame(window, bg="gray")
frame.pack(fill="both", expand=True)

Label(frame, text="Enter 1st Number:", bg="lightyellow").grid(row=0, column=0, padx=5, pady=3)
num1 = Entry(frame, width=12)
num1.grid(row=0, column=1)

Label(frame, text="Enter 2nd Number:", bg="lightyellow").grid(row=1, column=0, padx=5, pady=3)
num2 = Entry(frame, width=12)
num2.grid(row=1, column=1)

Button(frame, text="Add", width=3, command=add).grid(row=2, column=0, pady=5)
Button(frame, text="Subtract", width=7, command=subtract).grid(row=2, column=1, pady=5)
Button(frame, text="Multiply", width=7, command=multiply).grid(row=3, column=0, pady=5)
Button(frame, text="Division", width=7, command=divide).grid(row=3, column=1, pady=5)

window.mainloop()
