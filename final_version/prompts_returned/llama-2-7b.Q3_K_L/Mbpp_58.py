"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
from typing import Optional, List

def opposite_signs(x:int,y:int)->bool:
    x = abs(x); y=abs(y)
    return (x<0 and y>0 or x>0 and y<0)

