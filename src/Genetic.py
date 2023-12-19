import time
from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np
import random
from tkinter.messagebox import showerror

canvas_width = 600
canvas_height = 600
allTimes = []

def init_pop(pop_size , n = 8):
    return np.random.randint(n, size=(pop_size , n))

def calc_fitness(population , n=8):
    fitness_val = []
    for x in population:
        pentaly = 0 
        for i in range(n):
            r =x[i]
            for j in range(n):
                if i==j:
                    continue
                d = abs(i-j)
                if x[j] in [r , r-d ,r+d]:
                    pentaly+=1
        fitness_val.append(pentaly)
    return -1 * np.array(fitness_val)

def selection(population , fitness_vals):
    probs = fitness_vals.copy()
    probs += abs(probs.min()) +1 
    probs = probs = probs/probs.sum()
    N = len(population)
    indices = np.arange(N)
    selected_indices = np.random.choice(indices , size =N , p=probs)
    selected_population = population[selected_indices]
    return selected_population

def cross_over(parent1 , parent2 , pc, n =8):
    r = np.random.random()
    if r < pc:
        m = np.random.randint(1 ,n)
        child1 = np.concatenate([parent1[:m],  parent2[m:]])
        child2 = np.concatenate([parent2[:m],  parent1[m:]])
    else:
        child1  = parent1.copy()
        child2 = parent2.copy()
    return child1, child2

def mutation(individual , pm , n=8):
    r = np.random.random()
    if r < pm:
        m = np.random.randint(n)
        individual[m] = np.random.randint(n)
        return individual

def crossover_mutation(selected_pop , pc, pm , n=8):
    N = len(selected_pop)
    new_pop = np.empty((N,n) , dtype=int)
    for i in range(0, N ,2):
        parent1 = selected_pop[i]
        parent2 = selected_pop[i+1]
        child1 , child2 = cross_over(parent1, parent2, pc)
        new_pop[i] = child1 
        new_pop[i+1] = child2
    for i in range(N):
        mutation(new_pop[i], pm , n)
    return new_pop
        
def N_Queens(N , pop_size , max_generations , pc=0.70 , pm=0.01):
    population = init_pop(pop_size , N)
    best_fitness_overall = None
    for i_gen in range(max_generations):
        fitness_vals = calc_fitness(population , N)
        best_i = fitness_vals.argmax()
        best_fitness = fitness_vals[best_i]
        if best_fitness_overall is None or best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            best_solution = population[best_i].tolist()
        print(f'\ri_gen = {i_gen:06}  -f{-best_fitness_overall:03}'  , end='')
        if best_fitness == 0:
            print('\n Found optimal solution')
            break
        selected_pop = selection(population , fitness_vals)
        population = crossover_mutation(selected_pop, pc, pm, N)
    print()
    return best_solution

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
    solution = N_Queens(n, pop_size=100, max_generations=10000, pc=0.70, pm=0.3)
    print(solution)
    # solution = genetic_algorithm(n, 100, 1000, 0.1)
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