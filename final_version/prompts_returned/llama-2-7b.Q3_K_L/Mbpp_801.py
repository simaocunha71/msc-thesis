"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""
from typing import Optional

def test_three_equal(x: int, y: int, z:int):
    if x==y or x==z or y == z : return True
    else: return False
