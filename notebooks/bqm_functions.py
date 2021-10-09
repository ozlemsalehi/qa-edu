"""
This file contains all the functions used in the notebooks 
under the Binary Quadratic Model section.

Prepared by Akash Narayanan B
"""
from dimod import BinaryQuadraticModel

# Task 3

linear = {'x1': 3, 'x2': -1, 'x3': 10, 'x4': 7}
quadratic = {('x1', 'x2'): 2, ('x1', 'x3'): -5, ('x2', 'x3'): 3, ('x3', 'x4'): 11}
offset = 8
vartype = 'BINARY'