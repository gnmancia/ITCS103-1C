import tkinter as tk

def submit():
    first = first_name.get()
    middle = middle_name.get()
    last = last_name.get()
    gender = gender_var.get()

    age = 21

    id_window = tk.Toplevel(root)
    id_window.title("Student ID")
    id_window.geometry("260x300")
    id_window.configure(bg="lightyellow")

    title_color = "blue" if gender == "Male" else "red"

    title = tk.Label(id_window, text="STUDENT ID",
                     font=("Times New Roman", 16, "bold"),
                     bg="lightyellow",
                     fg=title_color)
    title.pack(pady=5)

    card = tk.Frame(id_window, bg="lightyellow", width=220, height=240)
    card.pack(pady=5)
    card.pack_propagate(False)

    icon = tk.Label(card, text="👤", font=("Arial", 50), bg="lightyellow")
    icon.pack(pady=5)

    name_label = tk.Label(card, text=f"Name: {first} {middle} {last}",
                          bg="lightyellow", anchor="w")
    name_label.pack(fill="x", padx=10, pady=5)

    age_label = tk.Label(card, text=f"Age: {age} years old",
                         bg="lightyellow", anchor="w")
    age_label.pack(fill="x", padx=10, pady=5)

    gender_label = tk.Label(card, text=f"Gender: {gender}",
                            bg="lightyellow", anchor="w",
                            fg=title_color)
    gender_label.pack(fill="x", padx=10, pady=5)

root = tk.Tk()
root.title("Profile Builder")
root.geometry("650x280")
root.configure(bg="lightyellow")

title = tk.Label(root, text="Profile Builder",
                 font=("Times New Roman", 18, "bold"),
                 bg="lightyellow")
title.pack(pady=10)

frame = tk.Frame(root, bg="lightyellow")
frame.pack(pady=5)

first_name = tk.Entry(frame, width=20)
first_name.grid(row=0, column=0, padx=10)
tk.Label(frame, text="First Name", bg="lightyellow").grid(row=1, column=0)

middle_name = tk.Entry(frame, width=20)
middle_name.grid(row=0, column=1, padx=10)
tk.Label(frame, text="Middle Name", bg="lightyellow").grid(row=1, column=1)

last_name = tk.Entry(frame, width=20)
last_name.grid(row=0, column=2, padx=10)
tk.Label(frame, text="Last Name", bg="lightyellow").grid(row=1, column=2)

birth_year = tk.Entry(frame, width=20)
birth_year.grid(row=2, column=0, padx=10, pady=10)
tk.Label(frame, text="Birth Year", bg="lightyellow").grid(row=3, column=0)

gender_var = tk.StringVar(value="Male")
tk.Label(frame, text="Gender", bg="lightyellow").grid(row=3, column=1)

tk.Radiobutton(frame, text="Male", variable=gender_var,
               value="Male", fg="blue", bg="lightyellow").grid(row=2, column=1)

tk.Radiobutton(frame, text="Female", variable=gender_var,
               value="Female", fg="lightyellow", bg="red").grid(row=2, column=2)

submit_btn = tk.Button(root, text="Submit",
                       font=("Arial", 12, "bold"),
                       command=submit)
submit_btn.pack(pady=15)

root.mainloop()