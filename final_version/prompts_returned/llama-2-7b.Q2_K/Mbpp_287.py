"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""

def square_Sum(n):
    if n <=1:return 0
    s = 2
    for i in range (2, int((n-2)/2)+1):
        s += i**2
    return s

print(square_Sum(10))