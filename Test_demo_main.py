import os
import sys
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from prediction_demo import predict_density  # Import the prediction function

# Global variables
selected_date = ""
day_of_week = ""
selected_hour = ""
selected_minute = ""
selected_period = ""
textarea_4 = None
image_3_id = None
image_4_id = None
image_5_id = None


def load_asset(path):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


# Function to open the calendar and select a date
def open_calendar():
    top = tk.Toplevel(window)
    top.geometry("400x400")
    top.title("Select a Date")

    cal = Calendar(top, selectmode="day", year=2023, month=10, day=19)
    cal.pack(pady=20)

    def grab_date():
        global selected_date
        global day_of_week
        selected_date = cal.get_date()
        date_obj = datetime.strptime(selected_date, "%m/%d/%y")
        day_of_week = date_obj.strftime("%A")
        textarea_4.delete(1.0, tk.END)
        textarea_4.tag_configure("center", justify="center")
        textarea_4.insert(tk.END, f"{selected_date}, {day_of_week}", "center")
        top.destroy()

    tk.Button(top, text="Select Date", command=grab_date).pack(pady=20)


# Function to open a time selection window
def open_time_selection():
    time_window = tk.Toplevel(window)
    time_window.geometry("300x300")
    time_window.title("Select Time")

    time_frame = tk.Frame(time_window)
    time_frame.pack(pady=20)

    # Hour selection
    hour_column = tk.Frame(time_frame)
    hour_column.pack(side=tk.LEFT, padx=10)
    tk.Label(hour_column, text="Hour:").pack()
    hour_spinbox = tk.Spinbox(hour_column, from_=1, to=12, format="%02.0f", width=2)
    hour_spinbox.pack()

    # Minute selection
    minute_column = tk.Frame(time_frame)
    minute_column.pack(side=tk.LEFT, padx=10)
    tk.Label(minute_column, text="Minute:").pack()
    minute_spinbox = tk.Spinbox(minute_column, from_=0, to=59, format="%02.0f", width=2)
    minute_spinbox.pack()

    # AM/PM selection
    am_pm_column = tk.Frame(time_frame)
    am_pm_column.pack(side=tk.LEFT, padx=10)
    tk.Label(am_pm_column, text="AM/PM:").pack()
    am_pm_var = tk.StringVar(value="AM")
    am_pm_dropdown = tk.OptionMenu(am_pm_column, am_pm_var, "AM", "PM")
    am_pm_dropdown.pack()

    def grab_time():
        global selected_hour
        global selected_minute
        global selected_period
        selected_hour = hour_spinbox.get()
        selected_minute = minute_spinbox.get()
        selected_period = am_pm_var.get()
        formatted_time = f"{selected_hour}:{selected_minute} {selected_period}"
        textarea_5.delete(1.0, tk.END)
        textarea_5.tag_configure("center", justify="center")
        textarea_5.insert(tk.END, formatted_time)
        textarea_5.tag_add("center", 1.0, tk.END)
        time_window.destroy()

    tk.Button(time_window, text="Select Time", command=grab_time).pack(pady=20)


def reset():
    global selected_date, day_of_week, selected_hour, selected_minute, selected_period
    global image_3_id, image_4_id, image_5_id

    # Reset variables
    selected_date = ""
    day_of_week = ""
    selected_hour = ""
    selected_minute = ""
    selected_period = ""

    # Clear text areas
    textarea_4.delete(1.0, tk.END)
    textarea_5.delete(1.0, tk.END)
    textarea_1.delete(1.0, tk.END)
    textarea_2.delete(1.0, tk.END)

    # Remove traffic condition images from the canvas if they exist
    if image_3_id:
        canvas.delete(image_3_id)
        image_3_id = None
    if image_4_id:
        canvas.delete(image_4_id)
        image_4_id = None
    if image_5_id:
        canvas.delete(image_5_id)
        image_5_id = None


# Function to convert the 12-hour format to 24-hour format
def convert_to_24_hour(hour, period):
    hour = int(hour)
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return hour


# Function to handle prediction
def handle_prediction():
    global day_of_week, selected_hour, selected_minute, selected_period
    global image_3_id, image_4_id, image_5_id

    # Convert the selected hour to 24-hour format

    hour_24 = convert_to_24_hour(selected_hour, selected_period)

    # Call the prediction function from prediction.py
    try:

        prediction = predict_density(day_of_week, hour_24, int(selected_minute))
        print(
            f"Prediction: Left Density = {prediction[0]}, Right Density = {prediction[1]}"
        )
        textarea_1.delete(1.0, tk.END)
        textarea_1.tag_configure("center", justify="center", font=("Montserrat", 24))
        textarea_1.insert(
            tk.END,
            f"Left Density = {prediction[0]:.2f}, Right Density = {prediction[1]:.2f}",
        )
        textarea_1.tag_add("center", 1.0, tk.END)
        # Calculate the average density
        left_density, right_density = prediction[0], prediction[1]
        average_density = (left_density + right_density) / 2

        if image_3_id:
            canvas.delete(image_3_id)
        if image_4_id:
            canvas.delete(image_4_id)
        if image_5_id:
            canvas.delete(image_5_id)

        # Determine traffic condition based on the average density
        if 0 <= average_density <= 6:
            traffic_condition = "Light Traffic"
            image_3_id = canvas.create_image(879, 782, image=image_3)

        elif 7 <= average_density <= 10:
            traffic_condition = "Moderate Traffic"
            image_4_id = canvas.create_image(879, 782, image=image_4)
        else:
            traffic_condition = "Heavy Traffic"
            image_5_id = canvas.create_image(879, 782, image=image_5)

        print(f"Traffic Condition: {traffic_condition}")
        textarea_2.delete(1.0, tk.END)
        textarea_2.tag_configure("center", justify="center")
        textarea_2.insert(
            tk.END,
            f"{traffic_condition}",
        )
        textarea_2.tag_add("center", 1.0, tk.END)

    except Exception as e:
        print(f"Error during prediction: {str(e)}")


# Create the main window
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

# Create buttons
button_1_image = tk.PhotoImage(file=load_asset("2.png"))
button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",
    activebackground="#2E2E2E",
    command=handle_prediction,
)
button_1.place(x=15, y=468, width=300, height=105)

button_2_image = tk.PhotoImage(file=load_asset("3.png"))
button_2 = tk.Button(
    image=button_2_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",
    activebackground="#2E2E2E",
    command=open_calendar,
)
button_2.place(x=15, y=170, width=300, height=105)

button_3_image = tk.PhotoImage(file=load_asset("4.png"))
button_3 = tk.Button(
    image=button_3_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",
    activebackground="#2E2E2E",
    command=open_time_selection,
)
button_3.place(x=15, y=319, width=300, height=105)

button_reset = tk.PhotoImage(file=load_asset("reset.png"))

button_4_reset = tk.Button(
    image=button_reset,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    bg="#2E2E2E",
    activebackground="#2E2E2E",
    command=reset,
)

button_4_reset.place(x=27, y=617, width=103, height=95)

# Create text areas
textarea_4 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
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

textarea_1 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 12),
)

textarea_1.place(x=427, y=398, width=834, height=80)  # numerical

textarea_2 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 35),
)

textarea_2.place(x=810, y=218, width=465, height=63)  # traffic intensity

textarea_3 = tk.Text(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    insertbackground="#000000",
    highlightthickness=0,
    font=("Montserrat", 12),
)

# textarea_3.place(x=427, y=736, width=834, height=263)  # statistical
image_2 = tk.PhotoImage(file=load_asset("7.png"))  # map

canvas.create_image(890, 748, image=image_2)

image_3 = tk.PhotoImage(file=load_asset("8.png"))  # green

# canvas.create_image(879, 782, image=image_3)

image_4 = tk.PhotoImage(file=load_asset("9.png"))  # yellow

# canvas.create_image(879, 782, image=image_4)

image_5 = tk.PhotoImage(file=load_asset("10.png"))  # red

# canvas.create_image(879, 782, image=image_5)

window.resizable(False, False)
window.mainloop()
