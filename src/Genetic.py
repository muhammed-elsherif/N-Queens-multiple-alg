import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from tkinter.messagebox import showerror

canvas_width = 600
canvas_height = 600
allTimes = []

def generate_population(population_size, board_size):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, board_size - 1) for _ in range(board_size)]
        population.append(chromosome)
    return population

def fitness(chromosome):
    conflicts = 0
    n = len(chromosome)
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(i - j) == abs(chromosome[i] - chromosome[j]):
                conflicts += 1
    return conflicts

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(0, n - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = random.randint(0, len(chromosome) - 1)
    return chromosome

def genetic_algorithm(board_size, population_size, generations, mutation_rate):
    population = generate_population(population_size, board_size)
    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            print("Solution found in generation", generation)
            return population[0]
        new_population = []
        for _ in range(population_size // 2):
            parent1 = population[random.randint(0, population_size // 2 - 1)]
            parent2 = population[random.randint(0, population_size // 2 - 1)]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population

    return None

def display_chessboard(board):
    n = len(board)
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
    solution = genetic_algorithm(n, 100, 1000, 0.1)
    end = time.time()

    allTimes.append(end - start)
    average = sum(allTimes) / len(allTimes)

    print(f"Time taken: {end - start} seconds")
    print(f"Average time taken: {average} seconds")
    if solution:
        display_chessboard(solution)
    else:
        print(f"No solution exists for {n}-Queens problem.")

def on_back_button_click():
    root.destroy()
    import Home

root = Tk()
root.title("N-Queens Solver(GeneticAlg)")

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