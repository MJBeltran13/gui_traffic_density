import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import joblib

# Load the data
data = pd.read_csv("./test/traffic_data.csv")

# Extract hour and minute from timestamp and create new columns
data["timestamp"] = pd.to_datetime(data["timestamp"])
data["hour"] = data["timestamp"].dt.hour
data["minute"] = data["timestamp"].dt.minute

# One-hot encode the 'day_of_the_week' feature
categorical_features = ["day_of_the_week"]
encoder = OneHotEncoder(sparse_output=False)  # Focus on day_of_the_week
encoded_features = encoder.fit_transform(data[categorical_features])

# Combine the encoded features with the original data
encoded_df = pd.DataFrame(
    encoded_features, columns=encoder.get_feature_names_out(categorical_features)
)
processed_data = pd.concat(
    [data[["left_density", "right_density", "hour", "minute"]], encoded_df], axis=1
)

# Split the data into features and targets
X = processed_data.drop(["left_density", "right_density"], axis=1)
y = processed_data[["left_density", "right_density"]]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model and encoder
joblib.dump(model, "./test/traffic_density_model.joblib")
joblib.dump(encoder, "./test/encoder.joblib")


# Function to make predictions
def predict_density(day_of_week, hour, minute):
    # Prepare the input data for prediction
    input_data = pd.DataFrame(
        [[day_of_week, hour, minute]], columns=["day_of_the_week", "hour", "minute"]
    )

    # One-hot encode the day_of_the_week column only
    input_encoded = encoder.transform(input_data[["day_of_the_week"]])

    # Ensure feature names match by aligning columns during prediction
    input_encoded_df = pd.concat(
        [
            pd.DataFrame(
                input_encoded,
                columns=encoder.get_feature_names_out(["day_of_the_week"]),
            ),
            input_data[["hour", "minute"]].reset_index(drop=True),
        ],
        axis=1,
    )

    # Reorder columns to match the order in the training data
    input_encoded_df = input_encoded_df[X.columns]

    # Make predictions
    prediction = model.predict(input_encoded_df)
    return prediction[0]


# Tkinter GUI for user input
def get_input():
    try:
        day_of_week = day_of_week_entry.get()
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())

        # Validate hour and minute inputs
        if not (0 <= hour <= 23):
            raise ValueError("Hour must be between 0 and 23.")
        if not (0 <= minute <= 59):
            raise ValueError("Minute must be between 0 and 59.")

        # Make prediction
        left_density, right_density = predict_density(day_of_week, hour, minute)

        # Insert the result into the table
        tree.insert(
            "",
            "end",
            values=(day_of_week, hour, minute, left_density, right_density),
        )
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Setting up Tkinter GUI
root = tk.Tk()
root.title("Traffic Density Forecasting")

# Input fields
tk.Label(root, text="Day of the Week:").grid(row=0, column=0)
day_of_week_entry = tk.Entry(root)
day_of_week_entry.grid(row=0, column=1)

tk.Label(root, text="Hour (0-23):").grid(row=1, column=0)
hour_entry = tk.Entry(root)
hour_entry.grid(row=1, column=1)

tk.Label(root, text="Minute (0-59):").grid(row=2, column=0)
minute_entry = tk.Entry(root)
minute_entry.grid(row=2, column=1)

# Submit button
submit_button = tk.Button(root, text="Predict", command=get_input)
submit_button.grid(row=3, column=0, columnspan=2)

# Setting up the Treeview for displaying results
columns = ("day_of_week", "hour", "minute", "left_density", "right_density")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.grid(row=4, column=0, columnspan=2)

# Define headings
tree.heading("day_of_week", text="Day of the Week")
tree.heading("hour", text="Hour")
tree.heading("minute", text="Minute")
tree.heading("left_density", text="Predicted Left Density")
tree.heading("right_density", text="Predicted Right Density")

# Adjust column width
for col in columns:
    tree.column(col, width=150)

root.mainloop()
