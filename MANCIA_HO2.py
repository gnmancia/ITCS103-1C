import tkinter as tk

root = tk.Tk()
root.title("Gerald Noel's Profile")
root.geometry("600x600")
root.configure(bg="lightyellow")

title = tk.Label(
    root,
    text="Student Profile",
    font=("Arial", 28, "bold"),
    bg="lightyellow"
)
title.pack(pady=20)

frame = tk.Frame(root, bg="lightyellow")
frame.pack(anchor="w", padx=40)

details = [
    ("Name", "Gerald Noel L. Mancia"),
    ("Age", "21 years old"),
    ("Course", "BSIT-1C"),
    ("Birthday", "December 21, 2004"),
]

for label, value in details:
    tk.Label(
        frame,
        text=f"{label} : {value}",
        font=("Arial", 14),
        bg="lightyellow",
        anchor="w"
    ).pack(anchor="w", pady=5)

tk.Label(
    frame,
    text="Motto :",
    font=("Arial", 14),
    bg="lightyellow",
    anchor="w"
).pack(anchor="w", pady=(20, 5))

tk.Label(
    frame,
    text="Keep moving forward, even on the days you feel afraid or exhausted.",
    font=("Arial", 13, "italic"),
    bg="lightyellow",
    wraplength=500,
    justify="left"
).pack(anchor="w")

root.mainloop()
