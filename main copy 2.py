import os
import sys
import tkinter as tk


def load_asset(path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


window = tk.Tk()
window.geometry("1440x1015")
window.configure(bg="#ffffff")
window.title("Untitled")

canvas = tk.Canvas(
    window,
    bg="#ffffff",
    width=1440,
    height=1015,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)

image_1 = tk.PhotoImage(file=load_asset("1.png"))

canvas.create_image(720, 507, image=image_1)

button_1_image = tk.PhotoImage(file=load_asset("2.png"))

button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",  # Normal background color
    fg="#2E2E2E",  # Normal text color (if there's text)
    activebackground="#2E2E2E",  # Background when pressed
    activeforeground="#2E2E2E",  # Text color when pressed
    command=lambda: print("button_1 has been pressed!"),
)

button_1.place(x=15, y=468, width=300, height=105)

button_2_image = tk.PhotoImage(file=load_asset("3.png"))

button_2 = tk.Button(
    image=button_2_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",  # Normal background color
    fg="#2E2E2E",  # Normal text color (if there's text)
    activebackground="#2E2E2E",  # Background when pressed
    activeforeground="#2E2E2E",  # Text color when pressed
    command=lambda: print("button_2 has been pressed!"),
)

button_2.place(x=15, y=170, width=300, height=105)

button_3_image = tk.PhotoImage(file=load_asset("4.png"))

button_3 = tk.Button(
    image=button_3_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",  # Normal background color
    fg="#2E2E2E",  # Normal text color (if there's text)
    activebackground="#2E2E2E",  # Background when pressed
    activeforeground="#2E2E2E",  # Text color when pressed
    command=lambda: print("button_3 has been pressed!"),
)

button_3.place(x=15, y=319, width=300, height=105)

button_4_image = tk.PhotoImage(file=load_asset("5.png"))

button_4 = tk.Button(
    image=button_4_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",  # Normal background color
    fg="#2E2E2E",  # Normal text color (if there's text)
    activebackground="#2E2E2E",  # Background when pressed
    activeforeground="#2E2E2E",  # Text color when pressed
    command=lambda: print("button_4 has been pressed!"),
)

button_4.place(x=19, y=617, width=126, height=105)

button_5_image = tk.PhotoImage(file=load_asset("6.png"))

button_5 = tk.Button(
    image=button_5_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",  # Normal background color
    fg="#2E2E2E",  # Normal text color (if there's text)
    activebackground="#2E2E2E",  # Background when pressed
    activeforeground="#2E2E2E",  # Text color when pressed
    command=lambda: print("button_5 has been pressed!"),
)

button_5.place(x=185, y=617, width=126, height=105)

textarea_1 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 12),
)

textarea_1.place(x=427, y=398, width=834, height=263)

textarea_2 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 12),
)

textarea_2.place(x=810, y=218, width=465, height=73)

textarea_3 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 12),
)

textarea_3.place(x=427, y=736, width=834, height=263)

window.resizable(False, False)
window.mainloop()
