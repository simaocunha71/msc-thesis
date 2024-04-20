"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""
import math
def cube_Sum(n):
    def helperFunction(x, y, z): #helper function
        if y == n:
            return [x*x*x] + [z for z in helperFunction(x+1, y-1, 0)]
        
    return helperFunction(-2, 0, -1)
print cube_Sum(3), ' are sum of first ', 3,' even natural numbers', "\n"
