import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('IndPopDen2011.csv')

# Prepare the data for the model
features = ['Population[55]', 'Male', 'Female', 'Rural[56]', 'Urban[56]', 'Area[57] (km2)']
target = 'Density (per km2)'
X = data[features]
y = data[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Function to predict population density
def predict_density():
    try:
        # Get user inputs
        population = float(entry_population.get())
        male = float(entry_male.get())
        female = float(entry_female.get())
        rural = float(entry_rural.get())
        urban = float(entry_urban.get())
        area = float(entry_area.get())
        
        # Prepare input data for prediction
        input_data = [[population, male, female, rural, urban, area]]
        predicted_density = model.predict(input_data)[0]
        
        # Show the result
        messagebox.showinfo("Prediction Result", f"Predicted Population Density: {predicted_density:.2f} per km²")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the Tkinter window
root = tk.Tk()
root.title("Population Density Predictor")
root.geometry("400x400")

# Create input fields
tk.Label(root, text="Population:").pack()
entry_population = tk.Entry(root)
entry_population.pack()

tk.Label(root, text="Male Population:").pack()
entry_male = tk.Entry(root)
entry_male.pack()

tk.Label(root, text="Female Population:").pack()
entry_female = tk.Entry(root)
entry_female.pack()

tk.Label(root, text="Rural Population:").pack()
entry_rural = tk.Entry(root)
entry_rural.pack()

tk.Label(root, text="Urban Population:").pack()
entry_urban = tk.Entry(root)
entry_urban.pack()

tk.Label(root, text="Area (km²):").pack()
entry_area = tk.Entry(root)
entry_area.pack()

# Create predict button
button_predict = tk.Button(root, text="Predict Population Density", command=predict_density)
button_predict.pack(pady=20)

# Run the Tkinter loop
root.mainloop()
