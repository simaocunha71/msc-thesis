"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""
import math

def bell_Number(n):
    if type(n) is not int:
        return n
    b = True
    s = 1
    while b:
        r = (s * (s + 1)) // 2
        if r < 0 or r >= n:
            break
        else:
            s += 1
    else:
        return False
    return r
