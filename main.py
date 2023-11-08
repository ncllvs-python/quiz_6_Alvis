import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from app.functions import add_numbers, subtract_numbers, divide_numbers, multiply_numbers
import os

# Global variables for name_entry, num1_entry, and num2_entry
name_entry = None
num1_entry = None
num2_entry = None

# Function to handle calculation and file saving
def calculate_and_save():
    global name_entry, num1_entry, num2_entry  # Access the global variables
    first_name = name_entry.get()
    last_name = simpledialog.askstring("Last Name", "Please enter your last name:")

    if not last_name:
        messagebox.showerror("Error", "Last name cannot be empty.")
        return

    filename = f"{last_name}.txt"
    a = float(num1_entry.get())
    b = float(num2_entry.get())

    with open(filename, "w") as file:
        file.write(f"This is {first_name}'s answer.\n")
        file.write(f"{a} + {b} = {add_numbers(a, b)}\n")
        file.write(f"{a} - {b} = {subtract_numbers(a, b)}\n")
        file.write(f"{a} / {b} = {divide_numbers(a, b)}\n")
        file.write(f"{a} * {b} = {multiply_numbers(a, b)}\n")

    messagebox.showinfo("Success", "Calculation saved to file.")

# Main function to create the GUI
def main():
    global name_entry, num1_entry, num2_entry  # Access the global variables

    # Create the main tkinter window
    root = tk.Tk()
    root.title("Math Operation Calculator")

    # Create labels, entry widgets, and a calculate button
    name_label = tk.Label(root, text="Your Name:")
    name_entry = tk.Entry(root)  # Update the global variable

    num1_label = tk.Label(root, text="Number 1:")
    num1_entry = tk.Entry(root)  # Update the global variable

    num2_label = tk.Label(root, text="Number 2:")
    num2_entry = tk.Entry(root)  # Update the global variable

    calculate_button = tk.Button(root, text="Calculate", command=calculate_and_save)

    # Pack the widgets
    name_label.pack()
    name_entry.pack()
    num1_label.pack()
    num1_entry.pack()
    num2_label.pack()
    num2_entry.pack()
    calculate_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
