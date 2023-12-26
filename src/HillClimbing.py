import math
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import time

allTimes = []

def generate_random_state(n):
    return random.sample(range(n), n)

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

def simulated_annealing(initial_state, max_itr, temperature):
    current_state = initial_state[:]
    current_conflicts = calculate_conflicts(current_state)

    for _ in range(max_itr):
        temperature *= 0.95
        if temperature <= 0.01:
            break

        neighbour = generate_random_neighbour(current_state)
        neighbour_conflicts = calculate_conflicts(neighbour)
        delta = neighbour_conflicts - current_conflicts

        if delta <= 0 or random.uniform(0, 1) < math.exp(-delta / temperature):
            current_state = neighbour
            current_conflicts = neighbour_conflicts

    return current_state

def solve_n_queens(n):
    max_itr = 500
    # initial_state = list(range(n))
    # initial_state = random.sample(range(n), n)
    # solution = hill_climbing(initial_state, max_itr)
    temperature = 100.0
    solutions = []

    for _ in range(5):  # Perform 5 random restarts
        initial_state = generate_random_state(n)
        solution = simulated_annealing(initial_state, max_itr, temperature)
        solutions.append((solution, calculate_conflicts(solution)))

    print('Initial state: ',initial_state)
    solutions.sort(key=lambda x: x[1])
    best_solution = solutions[0][0]
    return best_solution