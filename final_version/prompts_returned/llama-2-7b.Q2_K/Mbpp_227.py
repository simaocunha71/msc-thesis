"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""
import math
def min_of_three(a,b,c):
    n=int(math.fabs(a)-math.fabs(b))
    
    if (n > 0 and a < b):
        return a
    elif (n >= 0):
        return b  
    else:
        
        return c

min_of_three(10,20,0)==0