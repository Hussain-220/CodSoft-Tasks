import tkinter as tk
from tkinter import messagebox
import math


# Function to perform the calculation based on the operation
def calculate():
    try:
        operator = operator_var.get()

        # Determine the number of operands based on the operator
        if operator in ("+", "-", "*", "/", "^", "%"):
            # For basic arithmetic operations, we need two operands
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
        elif operator in ("sin", "cos", "tan", "log"):
            # For trigonometric functions and log, we need one operand
            num1 = float(entry_num1.get())
            num2 = None
        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            else:
                result = num1 / num2
        elif operator == "^":
            result = num1 ** num2
        elif operator == "%":
            result = num1 % num2
        elif operator == "log":
            result = math.log(num1, num2 if num2 else math.e)
        elif operator == "sin":
            result = math.sin(math.radians(num1))
        elif operator == "cos":
            result = math.cos(math.radians(num1))
        elif operator == "tan":
            result = math.tan(math.radians(num1))

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# Set up the main application window
root = tk.Tk()
root.title("Scientific Calculator")

# Create Entry widgets for numbers and operator choice
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

operator_var = tk.StringVar(value="+")
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/", "^", "%", "log", "sin", "cos", "tan")
operator_menu.pack(pady=5)

# Create 'Calculate' button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the main event loop
root.mainloop()