"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""
from typing import Optional
import math

def count_Pairs(i:int[::1], n:int=None):
    p = math.pow(n,(1/2))
    return len(set(x for x in i if p > (i[0] - 1) and p >= i[1]))
