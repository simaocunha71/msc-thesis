"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""

def square_sum(n):
    if n <=1: 
        return 0
    else:  
        total = n*((n-1)*2)/4
        print(total)
        return total

square_sum(7)