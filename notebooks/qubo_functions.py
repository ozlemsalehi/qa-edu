"""
This file contains all the functions used in the notebook 
QUBO_Mathematical_Definition.

Prepared by Akash Narayanan B
"""
import itertools
from ipywidgets import interact
import numpy as np


def task_1(x1, x2):
    value = 5*x1 + 7*x1*x2 - 3*x2
    return f"The value of the objective function is {value}."


def task_2(x1, x2, x3, x4):
    value = - 5*x1 - 3*x2 - 8*x3 - 6*x4 + 4*x1*x2 + 8*x1*x3 + 2*x2*x3 + 10*x3*x4
    return f"The value of the objective function is {value}."


def qubo_solver(Q_matrix):
    possible_values = {}
    # A list of all the possible permutations for x vector
    vec_permutations = itertools.product([0, 1], repeat=Q_matrix.shape[0])    
    
    for permutation in vec_permutations:
        x = np.array([[var] for var in permutation])         # Converts the permutation into a column vector
        value = (x.T).dot(Q_matrix).dot(x)
        possible_values[value[0][0]] = x                     # Adds the value and its vector to the dictionary
         
    min_value = min(possible_values.keys())                  # Lowest value of the objective function
    opt_vector = tuple(possible_values[min_value].T[0])      # Optimum vector x that produces the lowest value
     
    return f"The vector {opt_vector} minimizes the objective function to a value of {min_value}."