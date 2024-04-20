"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
from math import sqrt
def next_Perfect_Square(n):
    d = []
    for i in range(1, n/2+1):
        m = sqrt(i) + 1
        if (m * m) == i:
            d.append((m))
    return d[0]