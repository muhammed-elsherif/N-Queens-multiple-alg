import time
import tkinter as tk
from tkinter import ttk
import random
import heapq
from tkinter.messagebox import showerror

canvas_width = 600
canvas_height = 600
allTimes = []

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost

def is_safe(state, row, col, n):
    for i in range(row):
        if state[i] == col or \
           state[i] - i == col - row or \
           state[i] + i == col + row:
            return False
    return True

def heuristic(state, row, col, n):
    attacks = 0
    for i in range(row):
        if state[i]     == col or \
           state[i] - i == col - row or \
           state[i] + i == col + row:
            attacks += 1
    return attacks

def solve_n_queens(n):
    start_state = [-1] * n
    start_node = Node(start_state)
    start_node.cost = 0

    open_set = [start_node]

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state.count(-1) == 0:
            return current_node.state

        row = n - current_node.state.count(-1)
        cols = list(range(n))
        random.shuffle(cols)
        
        for col in cols:
            if is_safe(current_node.state, row, col, n):
                child_state = current_node.state.copy()
                child_state[row] = col
                child_node = Node(child_state, current_node)
                child_node.cost = heuristic(child_state, row, col, n)
                heapq.heappush(open_set, child_node)

    return None

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

def on_solve_button_click():
    n = int(entry.get())
    if n<3:
        showerror('Error', 'Please enter a valid number more than 3')
    start = time.time()
    board = solve_n_queens(n)
    end = time.time()

    allTimes.append(end - start)
    average = sum(allTimes) / len(allTimes)

    print(f"Time taken: {end - start} seconds")
    print(f"Average time taken: {average} seconds")

    if board:
        display_chessboard(board, n)
    else:
        print(f"No solution exists for {n}-Queens problem.")

def on_back_button_click():
    root.destroy()
    import Home

root = tk.Tk()
root.title("N-Queens Solver(BestFirstAlg)")

label = ttk.Label(root, text="Enter the number of Queens(N x N): ", font=("Arial", 16))
label.pack(pady=10, padx=10)

entry = ttk.Entry(root, font=("Arial", 16))
entry.pack()

button = ttk.Button(root, text="Solve", command=on_solve_button_click)
button.pack(pady=10)

button = ttk.Button(root, text="Back", command=on_back_button_click)
button.pack()

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

style = ttk.Style()
style.theme_use('clam')

root.mainloop()