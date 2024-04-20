"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""
from __future__ import division, print_function
import math

def square_Sum (n):
    if n < 1:
        return ""
    
    sum = 0
    for i in range(2, int(math.sqrt(n)) + 1, 2):
            s = i**2 #the square of the number
            sum += s
        
    print("square_Sum({}) returns: {}".format(n, str(sum)))