import time
from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np
import random
from tkinter.messagebox import showerror

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
        
def solve_n_queens(N):
    pop_size=100
    max_generations=10000
    pc=0.70 
    pm=0.01
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