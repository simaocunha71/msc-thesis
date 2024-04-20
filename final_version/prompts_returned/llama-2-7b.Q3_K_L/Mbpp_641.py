"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
import math
def is_nonagonal(n):
    res = [] # result
    for i in range(3, int(math.sqrt((n**2-1)*4))+1):
        x = i*i
        if (x**2-1) == n:
            res += [i]
        
    return sum(res)