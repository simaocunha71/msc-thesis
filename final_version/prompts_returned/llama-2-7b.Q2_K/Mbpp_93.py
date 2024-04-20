"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""
import math
def power(a, b):
    return a**math.pow(b, 1)
assert power(2,7) == 16 #10000016
assert power(-2, -7) == -1536 #111111536
assert power(4, 0) == 1