import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import time
import HillClimbing
import Backtracking
import BestFirst
import Genetic

canvas_width = 600
canvas_height = 600
allTimes = []

def on_alg_button_click(algorithm):
    n = int(entry.get())
    if n < 3:
        showerror('Error', 'Please enter a valid number more than 3')
    # Open the algorithm page based on the selected algorithm
    if algorithm == "Genetic Algorithm":
        genetic_algorithm_page(n)
    elif algorithm == "Best-First Algorithm":
        best_first_algorithm_page(n)
    elif algorithm == "Hill Climbing Algorithm":
        hill_climbing_algorithm_page(n)
    elif algorithm == "Backtracking Algorithm":
        backtracking_algorithm_page(n)


def genetic_algorithm_page(n):
    start = time.time()
    sol = Genetic.solve_n_queens(n)
    if sol:
        display_chessboard(sol, n)
    else:
        print(f"No solution exists for {n}-Queens problem.")
    end = time.time()
    allTimes.append(end - start)
    average = sum(allTimes) / len(allTimes)

    print(f"Time taken: {end - start} seconds")
    print(f"Average time taken: {average} seconds")

def best_first_algorithm_page(n):
    start = time.time()
    sol = BestFirst.solve_n_queens(n)
    if sol:
        display_chessboard(sol, n)
    else:
        print(f"No solution exists for {n}-Queens problem.")
    end = time.time()
    allTimes.append(end - start)
    average = sum(allTimes) / len(allTimes)

    print(f"Time taken: {end - start} seconds")
    print(f"Average time taken: {average} seconds")

def hill_climbing_algorithm_page(n):
    start = time.time()
    sol = HillClimbing.solve_n_queens(n)
    if sol:
        display_chessboard(sol, n)
    else:
        print(f"No solution exists for {n}-Queens problem.")
    end = time.time()
    allTimes.append(end - start)
    average = sum(allTimes) / len(allTimes)

    print(f"Time taken: {end - start} seconds")
    print(f"Average time taken: {average} seconds")

def backtracking_algorithm_page(n):
    start = time.time()
    sol = Backtracking.solve_n_queens(n)
    if sol:
       display_chessboard(sol, n)
    else:
        print(f"No solution exists for {n}-Queens problem.")
    end = time.time()
    allTimes.append(end - start)
    average = sum(allTimes) / len(allTimes)

    print(f"Time taken: {end - start} seconds")
    print(f"Average time taken: {average} seconds")

root = tk.Tk()
root.title("N-Queens Solver")

# Create a label and entry widgets for the number of Queens
label = ttk.Label(root, text="Enter the number of Queens(N x N): ", font=("Arial", 16))
label.grid(row=0, column=0, padx=10, pady=10)

entry = ttk.Entry(root, font=("Arial", 16))
entry.grid(row=0, column=1, padx=10, pady=10)

# Create a canvas for displaying the chessboard
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

style = ttk.Style()
style.theme_use('clam')

def display_chessboard(board, n):
    cell_size = min(canvas_width // n, canvas_height // n)

    canvas.delete("all")

    for i in range(n):
        for j in range(n):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = (j + 1) * cell_size, (i + 1) * cell_size
            color = "grey" if (i + j) % 2 == 0 else "brown"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

            if board[i] == j:
                canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2, text="♕", font=("Arial", cell_size // 2))
                
# Create a frame for the algorithm selection
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=2, pady=20)

# Create a label for instructions
label = tk.Label(frame, text="Choose an algorithm to solve the N-Queens problem:", font=("Arial", 14))
label.pack(pady=10)

# Create algorithm buttons
alg_buttons = [
    ("Genetic Algorithm", genetic_algorithm_page),
    ("Best-First Algorithm", best_first_algorithm_page),
    ("Hill Climbing Algorithm", hill_climbing_algorithm_page),
    ("Backtracking Algorithm", backtracking_algorithm_page)
]

for alg_name, alg_func in alg_buttons:
    button = tk.Button(frame, text=alg_name, font=("Arial", 12), width=25, height=2, command=lambda alg=alg_name: on_alg_button_click(alg))
    button.pack(pady=5)

root.mainloop()