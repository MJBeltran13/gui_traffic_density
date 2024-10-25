import os
import sys
import tkinter as tk
from tkcalendar import Calendar  # Import from tkcalendar
from datetime import datetime  # Import datetime for day of the week

# import prediction


def load_asset(path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


# Global variable to access textarea_4
textarea_4 = None

selected_date = ""
day_of_week = ""
selected_hour = ""
selected_minute = ""
selected_period = ""


# Function to open the calendar and select a date
def open_calendar():
    top = tk.Toplevel(window)  # Create a new window for the calendar
    top.geometry("400x400")
    top.title("Select a Date")

    cal = Calendar(top, selectmode="day", year=2023, month=10, day=19)
    cal.pack(pady=20)

    def grab_date():
        global selected_date
        global day_of_week
        selected_date = cal.get_date()  # Get selected date
        date_obj = datetime.strptime(
            selected_date, "%m/%d/%y"
        )  # Convert to datetime object
        day_of_week = date_obj.strftime("%A")  # Get the day of the week
        print(f"Selected Date: {selected_date}, Day: {day_of_week}")

        # Insert the selected date into textarea_4
        textarea_4.delete(1.0, tk.END)  # Clear previous text
        textarea_4.tag_configure("center", justify="center")
        textarea_4.insert(
            tk.END, f"{selected_date}, {day_of_week}", "center"
        )  # Insert new text

        top.destroy()  # Close the calendar window after selection

    # Button to confirm the date selection

    tk.Button(top, text="Select Date", command=grab_date).pack(pady=20)


# Function to open a time selection window
def open_time_selection():
    time_window = tk.Toplevel(window)  # Create a new window for time selection
    time_window.geometry("300x300")  # Adjusted height for AM/PM selection
    time_window.title("Select Time")

    # Create a frame for hour, minute, and AM/PM selection
    time_frame = tk.Frame(time_window)
    time_frame.pack(pady=20)

    # Column for hour selection
    hour_column = tk.Frame(time_frame)
    hour_column.pack(side=tk.LEFT, padx=10)

    # Label for hour selection
    tk.Label(hour_column, text="Hour:").pack()

    # Spinbox for hour selection
    hour_spinbox = tk.Spinbox(
        hour_column, from_=1, to=12, format="%02.0f", width=2
    )  # Changed range for 12-hour format
    hour_spinbox.pack()

    # Column for minute selection
    minute_column = tk.Frame(time_frame)
    minute_column.pack(side=tk.LEFT, padx=10)

    # Label for minute selection
    tk.Label(minute_column, text="Minute:").pack()

    # Spinbox for minute selection
    minute_spinbox = tk.Spinbox(minute_column, from_=0, to=59, format="%02.0f", width=2)
    minute_spinbox.pack()

    # Column for AM/PM selection
    am_pm_column = tk.Frame(time_frame)
    am_pm_column.pack(side=tk.LEFT, padx=10)

    # Label for AM/PM selection
    tk.Label(am_pm_column, text="AM/PM:").pack()

    # Dropdown for AM/PM selection
    am_pm_var = tk.StringVar(value="AM")
    am_pm_dropdown = tk.OptionMenu(am_pm_column, am_pm_var, "AM", "PM")
    am_pm_dropdown.pack()

    def grab_time():
        global selected_hour
        global selected_minute
        global selected_period
        selected_hour = hour_spinbox.get()
        selected_minute = minute_spinbox.get()
        selected_period = am_pm_var.get()  # Get AM/PM selection
        formatted_time = (
            f"{selected_hour}:{selected_minute} {selected_period}"  # Format the time
        )
        print(f"Selected Time: {formatted_time}")
        textarea_5.delete(1.0, tk.END)  # Clear previous text
        textarea_5.tag_configure("center", justify="center")
        textarea_5.insert(tk.END, formatted_time)  # Insert new text with AM/PM format
        textarea_5.tag_add("center", 1.0, tk.END)
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
    command=lambda: print(
        day_of_week, selected_date, selected_hour, selected_minute, selected_period
    ),
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
    font=("Montserrat", 35),
)

textarea_2.place(x=810, y=218, width=465, height=63)

textarea_3 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 12),
)

# textarea_3.place(x=427, y=736, width=834, height=263)

# Initialize textarea_4 as a global variable
textarea_4 = tk.Text(
    bd=0,
    bg="#ffffff",  # Match the window's background color
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,  # No border thickness
    highlightbackground="#ffffff",  # Match highlight background
    font=("Montserrat", 35),
)

textarea_4.place(x=450, y=113, width=472, height=63)

textarea_5 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 40),
)

textarea_5.place(x=943, y=113, width=332, height=63)

window.resizable(False, False)
window.mainloop()
