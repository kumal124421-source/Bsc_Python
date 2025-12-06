# data_visualizer.py
# Mini Project – Basic Data Visualizer
# Course: Foundations of Programming using Python (ETCCFP103)

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Task 1: Load Dataset
# -----------------------------

# Load CSV file
data = pd.read_csv("temperature.csv")

# Display first 10 rows
print("First 10 rows of the dataset:")
print(data.head(10))

# -----------------------------
# Task 2: Data Cleaning
# -----------------------------

# Check missing values
print("\nMissing values before cleaning:")
print(data.isnull().sum())

# Fill missing temperature values with mean
if "Temperature" in data.columns:
    data["Temperature"].fillna(data["Temperature"].mean(), inplace=True)

# Drop rows if any important column is missing
data.dropna(inplace=True)

# Confirm cleanliness
print("\nMissing values after cleaning:")
print(data.isnull().sum())

# -----------------------------
# Task 3: Line Plot
# -----------------------------

plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Variation Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_plot.png")
plt.close()

print("\nSaved: line_plot.png")

# -----------------------------
# Task 4: Bar Chart
# -----------------------------

# Convert Date column to datetime (if not already)
data["Date"] = pd.to_datetime(data["Date"])

# Group by month and take average temperature
data["Month"] = data["Date"].dt.month
monthly_avg = data.groupby("Month")["Temperature"].mean()

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind="bar")
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.title("Average Monthly Temperature")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

print("Saved: bar_chart.png")

# -----------------------------
# Final Output
# -----------------------------

print("\nBoth plots saved successfully.")
