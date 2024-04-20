"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""
import math
def perfect_squares(a, b):
    ret = set()
    for i in range(a - 1, b+1):
        if (math.sqrt(i) % 1 == 0 and i > a + 1):
            ret.add((math.sqrt(i))*2)
    return list(ret)
