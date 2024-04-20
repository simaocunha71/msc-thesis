"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
import math

def sum_of_product(n):
    x = 0
    for i in range (1, n+1): # (start from 1 till the end of the sequence )
        p = binomial(i,i-1)
        print("p", end='')
        while math.isnan(x + p):
            x += p
    return sum_of_product(n+1) - sum_of_product(3) # (start from 4 till the end of the sequence )
    
print sum_of_product(6)