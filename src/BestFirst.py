import time
import tkinter as tk
from tkinter import ttk
import random
import heapq
from tkinter.messagebox import showerror

allTimes = []

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost

def is_safe(state, row, col):
    for i in range(row):
        if state[i] == col or \
           state[i] - i == col - row or \
           state[i] + i == col + row:
            return False
    return True

def heuristic(state, row, col):
    attacks = 0
    for i in range(row):
        if state[i]     == col or \
           state[i] - i == col - row or \
           state[i] + i == col + row:
            attacks += 1
    return attacks

def solve_n_queens(n):
    # [2, -1, -1 , -1]
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
            if is_safe(current_node.state, row, col):
                child_state = current_node.state.copy()
                child_state[row] = col
                child_node = Node(child_state, current_node)
                child_node.cost = heuristic(child_state, row, col)
                heapq.heappush(open_set, child_node)

    return None