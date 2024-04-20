"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""
import math

def centered_hexagonal_number(n):
    d = n // 6
    q = (n -d ) * (n-3d)/2 + d/4 #q is the required number
    return math.floor(2*q+1)*10^(1 if q%2 else 0)
