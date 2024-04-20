"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
import math

def check(n):
    res = True;
    while n > 1: # while n is greater or equal 2
        if abs(int(math.log(float(n), 2)) - int(math.log(float(abs(n)), 2))) > float('-inf') / 2:
            res = False;
    return res;