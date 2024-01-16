import random
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

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
    for col in random.sample(range(n), n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    best_solution = []
    if not solve_n_queens_util(board, 0, n):
        print(f"No solution exists for {n}-Queens problem.")
        return False

    print(f"Randomized solution for {n}-Queens problem:")
    for i in range(n):   
        print(" ".join(str(x) for x in board[i]))
        for j in range(n):
            if board[i][j] == 1:
                best_solution.append(j)
    return best_solution