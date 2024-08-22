import tkinter as tk
from random import randint
from math import log, ceil

def start_game():
    lower_bound = int(lower_entry.get())
    upper_bound = int(upper_entry.get())
    
    if lower_bound < 0 or upper_bound < 0:
        result_label.config(text="Please enter positive integers only.")
        return
    
    if upper_bound <= lower_bound:
        result_label.config(text="Upper bound should be greater than lower bound.")
        return
    
    random_number = randint(lower_bound, upper_bound)
    number_of_guesses = ceil(log(upper_bound - lower_bound + 1, 2))
    result_label.config(text=f"Number generated! You have {number_of_guesses} guesses.")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create and place widgets
tk.Label(root, text="Lower Bound:").grid(row=0, column=0)
lower_entry = tk.Entry(root)
lower_entry.grid(row=0, column=1)

tk.Label(root, text="Upper Bound:").grid(row=1, column=0)
upper_entry = tk.Entry(root)
upper_entry.grid(row=1, column=1)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
