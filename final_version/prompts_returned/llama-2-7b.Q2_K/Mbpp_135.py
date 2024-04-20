"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""
import math
def hexagonal_num(n):
    if int(n/2)==int((n-1)/sqrt(3)):
        return ((int(n/2)-1)**2+6*int((n-1)/sqrt(3))**2)+(4+(n-1))
    else:
        return 0
#assert hexagonal_num(15) == 2987


hexagonal_num(10)