import os
import sys
import tkinter as tk
from tkcalendar import Calendar  # Import from tkcalendar
from datetime import datetime  # Import datetime for day of the week


def load_asset(path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


# Function to open the calendar and select a date
def open_calendar():
    top = tk.Toplevel(window)  # Create a new window for the calendar
    top.geometry("400x400")
    top.title("Select a Date")

    cal = Calendar(top, selectmode="day", year=2023, month=10, day=19)
    cal.pack(pady=20)

    def grab_date():
        selected_date = cal.get_date()  # Get selected date
        date_obj = datetime.strptime(
            selected_date, "%m/%d/%y"
        )  # Convert to datetime object
        day_of_week = date_obj.strftime("%A")  # Get the day of the week
        print(f"Selected Date: {selected_date}, Day: {day_of_week}")
        top.destroy()  # Close the calendar window after selection

    # Button to confirm the date selection
    tk.Button(top, text="Select Date", command=grab_date).pack(pady=20)


# Function to open a time selection window
def open_time_selection():
    time_window = tk.Toplevel(window)  # Create a new window for time selection
    time_window.geometry("300x250")
    time_window.title("Select Time")

    # Create a frame for hour and minute selection
    time_frame = tk.Frame(time_window)
    time_frame.pack(pady=20)

    # Column for hour selection
    hour_column = tk.Frame(time_frame)
    hour_column.pack(side=tk.LEFT, padx=10)

    # Label for hour selection
    tk.Label(hour_column, text="Hour:").pack()

    # Spinbox for hour selection
    hour_spinbox = tk.Spinbox(hour_column, from_=0, to=23, format="%02.0f", width=2)
    hour_spinbox.pack()

    # Column for minute selection
    minute_column = tk.Frame(time_frame)
    minute_column.pack(side=tk.RIGHT, padx=10)

    # Label for minute selection
    tk.Label(minute_column, text="Minute:").pack()

    # Spinbox for minute selection
    minute_spinbox = tk.Spinbox(minute_column, from_=0, to=59, format="%02.0f", width=2)
    minute_spinbox.pack()

    def grab_time():
        selected_hour = hour_spinbox.get()
        selected_minute = minute_spinbox.get()
        print(f"Selected Time: {selected_hour}:{selected_minute}")
        time_window.destroy()  # Close the time selection window after selection

    # Button to confirm the time selection
    tk.Button(time_window, text="Select Time", command=grab_time).pack(pady=20)


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
    command=open_calendar,  # Open the calendar on button press
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
    command=open_time_selection,  # Open the time selection on button press
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

textarea_4 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 40),
)

textarea_4.place(x=450, y=113, width=332, height=73)

textarea_5 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 40),
)

textarea_5.place(x=943, y=113, width=332, height=73)


window.resizable(False, False)
window.mainloop()
