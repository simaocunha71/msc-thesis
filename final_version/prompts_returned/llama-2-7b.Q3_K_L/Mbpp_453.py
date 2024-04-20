"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""
from typing import Optional, Union

def sumofFactors(x: int=None) -> int:
    if x is None or not isinstance(x,int):
        return -1
    
    f = [i for i in range(1,x+1)]
    if len(f) == 1 and f[0]%2 != 0:
       return sumofFactors(x-f[0]) + f[0]*f[0]/2 #sum of factors is always odd so we have to consider half the factor
    
    s = 1
    for i in range(2, len(f)):
        if (i%2 == 1 and x % f[i] != 0) or (i%2 == 0 and x % f[i] == 0):
            s += f[i]/2   # sum of even factors is always odd so we have to consider half the factor   
        if s > x: return s
    
    return -1