import random
import tkinter as tk
from tkinter import ttk

def generate_random_neighbour(current_state):
    neighbour = current_state[:]
    index1 = random.randint(0, len(neighbour) - 2)
    index2 = random.randint(0, len(neighbour) - 2)
    neighbour[index1], neighbour[index2] = neighbour[index2], neighbour[index1]
    return neighbour

def calculate_conflicts(current_state):
    conflicts = 0
    size = len(current_state)
    for i in range(size):
        for j in range(i + 1, size):
            if current_state[i] == current_state[j] or abs(current_state[i] - current_state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing(initial_state, max_itr):
    current_state = initial_state[:]
    current_conflicts = calculate_conflicts(current_state)
    for _ in range(max_itr):
        neighbour = generate_random_neighbour(current_state)
        neighbour_conflicts = calculate_conflicts(neighbour)
        if neighbour_conflicts < current_conflicts:
            current_state = neighbour
            current_conflicts = neighbour_conflicts
    return current_state

def solve_n_queens(n):
    max_itr = 100
    # initial_state = list(range(n))
    initial_state = random.sample(range(n), n)
    sol = hill_climbing(initial_state, max_itr)
    display_chessboard([[1 if i == col else 0 for col in sol] for i in range(n)], n)

def display_chessboard(board, n):
    cell_size = 35
    canvas.delete("all")

    for i in range(n):
        for j in range(n):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = (j + 1) * cell_size, (i + 1) * cell_size
            color = "white" if (i + j) % 2 == 0 else "red"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

            if board[i][j] == 1:
                canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2, text="♕", font=("Arial", cell_size // 2))

def on_button_click():
    n = int(entry.get())
    # board = 
    solve_n_queens(n)
    # if board:
    #     display_chessboard(board, n)
    # else:
    #     print(f"No solution exists for {n}-Queens problem.")

root = tk.Tk()
root.title("N-Queens Solver(HillClimbingAlg)")

label = tk.Label(root, text="Enter the number of Queens(N x N): ")
label.pack()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Solve", command=on_button_click)
button.pack()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

style = ttk.Style()
style.theme_use('clam')

root.mainloop()