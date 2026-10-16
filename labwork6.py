import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Labwork 6a: Basic Plotting ---
print("--- Starting Labwork 6a ---")
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="Sin Curve", color="blue")
plt.title("Line Plot - Labwork 6a")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.legend()

# Save line plot as PDF
plt.savefig("po6.pdf")
plt.close()
print("[SUCCESS] Saved plot to 'po6.pdf'")

# --- Labwork 6b: Data Processing & Visualizations ---
print("\n--- Starting Labwork 6b ---")

# Generate sample dataset if scores6.csv does not exist
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "Math": [85, 90, 78, 92, 88, 70, 95],
    "Python": [88, 92, 80, 85, 90, 75, 98],
    "DB": [90, 85, 82, 88, 94, 72, 91],
}
df = pd.DataFrame(data)
df.to_csv("scores6.csv", index=False)
print("[INFO] Created dataset 'scores6.csv'")

# 1. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(df["Math"], df["Python"], color="purple")
plt.title("Math vs Python Scores")
plt.xlabel("Math Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.savefig("scattered6.png")
plt.close()
print("[SUCCESS] Saved scatter plot to 'scattered6.png'")

# 2. Histograms
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
df["Math"].plot(
    kind="hist", ax=axes[0], title="Math Scores", color="skyblue", edgecolor="black"
)
df["Python"].plot(
    kind="hist",
    ax=axes[1],
    title="Python Scores",
    color="lightgreen",
    edgecolor="black",
)
df["DB"].plot(
    kind="hist", ax=axes[2], title="DB Scores", color="salmon", edgecolor="black"
)
plt.tight_layout()
plt.savefig("histo6.png")
plt.close()
print("[SUCCESS] Saved histograms to 'histo6.png'")

# 3. Box Plot
plt.figure(figsize=(6, 4))
df[["Math", "Python", "DB"]].plot(kind="box")
plt.title("Box Plot for Math, Python, and DB")
plt.ylabel("Marks")
plt.grid(True)
plt.savefig("box6.png")
plt.close()
print("[SUCCESS] Saved box plot to 'box6.png'")

print("\n--- Labwork 6 Execution Complete ---")