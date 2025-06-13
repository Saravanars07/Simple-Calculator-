import tkinter as tk
from tkinter import messagebox

# Store calculation history
history = []

def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

def clear_display():
    display_var.set("0")

def calculate_result():
    try:
        result = eval(display_var.get())
        # Save calculation to history
        history.append(f"{display_var.get()} = {result}")
        display_var.set(result)
    except Exception:
        display_var.set("Error")

def working_clear():
    current_text = display_var.get()
    if len(current_text) > 1:
        display_var.set(current_text[:-1])
    else:
        display_var.set("0")

# Function to show history in a popup window
def show_history():
    if history:
        history_text = "\n".join(history)
    else:
        history_text = "No history yet."
    messagebox.showinfo("Calculation History",history_text)

parent = tk.Tk()
parent.title("Calculator")

display_var = tk.StringVar()
display_var.set("0")

display_label = tk.Label(parent, textvariable=display_var,font=("Arial", 24),anchor="e",bg="lightgray", padx=10, pady=10)
display_label.grid(row=0, column=0, columnspan=4)

button_layout=[
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in button_layout:
    if text == "=":
        button = tk.Button(
            parent, text=text, padx=20, pady=20, font=("Arial", 18),
            command=calculate_result,
            activebackground="red", activeforeground="white"
        )
    else:
        button = tk.Button(
            parent, text=text, padx=20, pady=20, font=("Arial", 18),
            command=lambda t=text: update_display(t),
            activebackground="red", activeforeground="white"
        )
    button.grid(row=row, column=col)

for (text, row, col) in button_layout:
    if text == "=":
        button = tk.Button(parent,text=text,padx=20,pady=20,font=("Arial", 18), command=calculate_result)
    else:
        button=tk.Button(parent, text=text, padx=20, pady=20,font=("Arial",18),command=lambda t=text: update_display(t))
    button.grid(row=row, column=col)

clear_button=tk.Button(parent, text="Clear", padx=2, pady=2,font=("Arial",18),command=clear_display)
clear_button.grid(row=5, column=0, sticky="we")

working_button=tk.Button(parent,text="AC",padx=2,pady=2,font=("Arial",18),command=working_clear)
working_button.grid(row=5,column=1,sticky="we")

# Add the "History" button
history_button = tk.Button(parent,text="History",padx=2,pady=2,font=("Arial",18),command=show_history)
history_button.grid(row=5, column=2, columnspan=2, sticky="we")

parent.mainloop()
