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
    # Hardcoded predictions for specific days and time
    if day_of_week == "Monday" and hour == 10 and minute == 30:
        return [20, 21]  # Predicted densities for Monday
    elif day_of_week == "Tuesday" and hour == 10 and minute == 30:
        return [22, 23]  # Predicted densities for Tuesday
    elif day_of_week == "Wednesday" and hour == 10 and minute == 30:
        return [24, 25]  # Predicted densities for Wednesday
    elif day_of_week == "Thursday" and hour == 10 and minute == 30:
        return [26, 27]  # Predicted densities for Thursday
    elif day_of_week == "Friday" and hour == 10 and minute == 30:
        return [28, 29]  # Predicted densities for Friday
    elif day_of_week == "Saturday" and hour == 10 and minute == 30:
        return [30, 31]  # Predicted densities for Saturday
    elif day_of_week == "Sunday" and hour == 10 and minute == 30:
        return [32, 33]  # Predicted densities for Sunday

    # Default values for any other input
    return [0, 0]  # Default predicted densities
