import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    try:
        # Convert the input to a float and calculate Fahrenheit
        celsius = float(celsius)
        fahrenheit = (celsius * 9/5) + 32
        return round(fahrenheit, 2)  # Return the result rounded to 2 decimal places
    except ValueError:
        return None  # Return None if the input is not a valid number

# Function to handle the conversion
def on_convert_button_click(entry, result_label):
    celsius = entry.get()
    
    # Input validation: Check if the entry is empty or invalid
    if celsius == "":
        messagebox.showerror("Input Error", "Please enter a value.")
        return
    
    result = convert_celsius_to_fahrenheit(celsius)
    
    if result is None:
        messagebox.showerror("Input Error", "Invalid number. Please enter a valid number.")
    else:
        result_label.config(text=f"{celsius}°C = {result}°F")  # Display the result in the label

# Function to clear the entry and result label
def on_clear_button_click(entry, result_label):
    entry.delete(0, tk.END)  # Clear the entry box
    result_label.config(text="")  # Clear the result label

# Function to exit the application
def on_exit_button_click(root):
    root.quit()  # Exit the application

# Function to create the first (main) window
def create_main_window():
    root = tk.Tk()  # Create the main window
    root.title("Celsius to Fahrenheit Converter")  # Title of the window
    root.geometry("400x400")  # Size of the window
    
    # Label 1: Instructions
    label1 = tk.Label(root, text="Enter Celsius to Convert to Fahrenheit", font=("Arial", 14))
    label1.grid(row=0, column=0, columnspan=2, pady=10)

    # Label 2: Input label
    label2 = tk.Label(root, text="Celsius:")
    label2.grid(row=1, column=0, pady=5, padx=10)

    # Entry field for Celsius value
    celsius_entry = tk.Entry(root, font=("Arial", 12))
    celsius_entry.grid(row=1, column=1, pady=5)

    # Result label (initially empty)
    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

    # Button 1: Convert
    convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=lambda: on_convert_button_click(celsius_entry, result_label))
    convert_button.grid(row=3, column=0, pady=10)

    # Button 2: Clear
    clear_button = tk.Button(root, text="Clear", font=("Arial", 12), command=lambda: on_clear_button_click(celsius_entry, result_label))
    clear_button.grid(row=3, column=1, pady=10)

    # Button 3: Exit
    exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=lambda: on_exit_button_click(root))
    exit_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Add images for Celsius and Fahrenheit
    img_celsius = PhotoImage(file="C:\\Users\\gagei\\Downloads\\celsius.gif")
    img_fahrenheit = PhotoImage(file="C:\\Users\\gagei\\Downloads\\faren.gif")
    # Resize images to fit in the window (scale them down)
    img_celsius_resized = img_celsius.subsample(7, 7)  # Adjust the scale factor (4, 4) as needed
    img_fahrenheit_resized = img_fahrenheit.subsample(7, 7)  # Adjust the scale factor (4, 4) as needed

    # Display the resized images in the window
    img_label_celsius = tk.Label(root, image=img_celsius_resized)
    img_label_celsius.image = img_celsius_resized  # Keep a reference to the image to prevent it from being garbage collected
    img_label_celsius.grid(row=0, column=2, padx=10)

    img_label_fahrenheit = tk.Label(root, image=img_fahrenheit_resized)
    img_label_fahrenheit.image = img_fahrenheit_resized  # Keep a reference to the image to prevent it from being garbage collected
    img_label_fahrenheit.grid(row=1, column=2, padx=10)

    root.mainloop()  # Run the main loop for the Tkinter application

# Run the application
if __name__ == "__main__":
    create_main_window()

