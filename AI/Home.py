import tkinter as tk


def on_alg_button_click(algorithm):
    # Open the algorithm page based on the selected algorithm
    if algorithm == "Genetic Algorithm":
        open_genetic_algorithm_page()
    elif algorithm == "Best-First Algorithm":
        open_best_first_algorithm_page()
    elif algorithm == "Hill Climbing Algorithm":
        open_hill_climbing_algorithm_page()
    elif algorithm == "Backtracking Algorithm":
        open_backtracking_algorithm_page()


def open_genetic_algorithm_page():
    root.destroy()
    import Genetic

def open_best_first_algorithm_page():
    root.destroy()
    import BestFirst

def open_hill_climbing_algorithm_page():
    root.destroy()
    import HillClimbing

def open_backtracking_algorithm_page():
    root.destroy()
    import Backtracking


root = tk.Tk()
root.title("N-Queens Solver")

# Create a frame for the algorithm selection
frame = tk.Frame(root)
frame.pack(pady=20)

# Create a label for instructions
label = tk.Label(frame, text="Choose an algorithm to solve the N-Queens problem:", font=("Arial", 14))
label.pack(pady=10)

# Create algorithm buttons
alg_buttons = [
    ("Genetic Algorithm", open_genetic_algorithm_page),
    ("Best-First Algorithm", open_best_first_algorithm_page),
    ("Hill Climbing Algorithm", open_hill_climbing_algorithm_page),
    ("Backtracking Algorithm", open_backtracking_algorithm_page)
]

for alg_name, alg_func in alg_buttons:
    button = tk.Button(frame, text=alg_name, font=("Arial", 12), width=25, height=2, command=lambda alg=alg_name: on_alg_button_click(alg))
    button.pack(pady=5)

root.mainloop()