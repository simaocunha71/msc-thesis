"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""
from math import sqrt
def square_Sum(n):
    sq = sqrt(n)
    return (3 * sq ** 3 + sq * (4**2)) / 6