import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

canvas_width = 600
canvas_height = 600
allTimes = []

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens_util(board, row + 1, n):
                return True

            board[row][col] = 0

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print(f"No solution exists for {n}-Queens problem.")
        return False

    print(f"Solution for {n}-Queens problem:")
    for i in range(n):
        print(" ".join(str(x) for x in board[i]))
    
    display_chessboard(board, n)  
    
    return True

def display_chessboard(board, n):
    cell_size = min(canvas_width // n, canvas_height // n) 

    canvas.delete("all")  

    for i in range(n):
        for j in range(n):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = (j + 1) * cell_size, (i + 1) * cell_size
            color = "grey" if (i + j) % 2 == 0 else "brown"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

            if board[i][j] == 1:
                canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2, text="♕", font=("Arial", cell_size // 2))

def on_solve_button_click():
    n = int(entry.get())
    if n<3:
        showerror('Error', 'Please enter a valid number more than 3')

    start = time.time()
    solve_n_queens(n)
    end = time.time()

    allTimes.append(end - start)
    average = sum(allTimes) / len(allTimes)

    print(f"Time taken: {end - start} seconds")
    print(f"Average time taken: {average} seconds")

def on_back_button_click():
    root.destroy()
    import Home

root = tk.Tk()
root.title("N-Queens Solver(BacktrackingAlg)")

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