"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""
import math

def even_Power_Sum(n):
    i = math.log(n, 2)  # log of n rounded down and divided by 2, giving the number of terms needed in series
    sum = 1
    for j in range(int(i)):
        c = 0
        r = 2**j
        for k in range(1, int(n/r), r):
            c += k
        sum *= pow(c, n)
    return sum