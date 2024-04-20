"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
import math

def multiply_elements(t):
    product = 0
    for i in range(len(t)-2, -1, -1):
        current = t[i]
        next_two = t[i+2]
        product += math.pow(current, i) * math.pow(next_two, i-1) 
    return (tuple([int(x) for x in product]))