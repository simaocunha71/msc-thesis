"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""
import math

def odd_num_sum(n):
    return ((1+math.pow(3, int(math.log(3)/log(2))**n)))*((1+math.pow(5,int(math.log(5)/log(2))**n)))*((1+math.pow(7,int(math.log(7)/log(2))**n)))
