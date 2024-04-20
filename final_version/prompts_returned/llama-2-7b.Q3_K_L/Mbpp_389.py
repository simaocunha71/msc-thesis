"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""
import math
def find_lucas(n):
    c = len(str(n)) - 1
    
    if c %2 !=0:
        return str(int(math.pow(n,c)))[1:]
    else:
        s = n**c - n**(c-1)
        return int(s)
