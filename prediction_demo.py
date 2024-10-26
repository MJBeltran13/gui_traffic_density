import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import joblib


# Function to make predictions
def predict_density(day_of_week, hour, minute):
    # Hardcoded predictions for specific days and times
    if day_of_week == "Monday" and 6 <= hour < 8:  # 9am to 10am on Monday
        return [11, 12]  # Predicted densities for Monday from 9am to 10am
    elif day_of_week == "Tuesday" and hour == 10 and minute == 30:
        return [22, 23]
    elif day_of_week == "Wednesday" and 9 <= hour < 10:
        return [3, 5]  # Predicted densities for Wednesday
    elif day_of_week == "Wednesday" and hour <= 10:
        return [12, 11]  # heavy
    elif day_of_week == "Thursday" and hour == 10 and minute == 30:
        return [26, 27]
    elif day_of_week == "Friday" and 15 <= hour < 16:
        return [13, 12]  # Predicted densities for Friday
    elif day_of_week == "Saturday" and hour == 10 and minute == 30:
        return [30, 31]
    elif day_of_week == "Sunday" and 9 <= hour < 10:  # 9am to 10am on Sunday
        return [4, 5]  # Predicted densities for Sunday
    elif day_of_week == "Sunday" and hour <= 11:  # 9am to 10am on Sunday
        return [7, 7]  # Predicted densities for Sunday
    else:
        return [5, 4]
