import tkinter as eze

window = eze.Tk()

window.title("BSIT 1C")
window.geometry("400x400")
window.resizable(False,False)
window.configure(bg="lightyellow",cursor="hand2")

label =eze.Label(window, text="Hello,world!",font=("League Spartan",35,"bold"),fg="white",bg="black",anchor="s")


label2 =eze.Label(window, text="BSIT 1C - 2025-2026",font=("Arial",20,"italic"),fg="black",bg="lightblue",anchor="n")

label2.pack(padx=(10,0),pady=(10,0))
label.pack(padx=(10,0),pady=(20,0))

window.mainloop()