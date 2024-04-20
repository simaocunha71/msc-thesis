"""
Write a python function to toggle bits of the number except the first and the last bit. 
assert toggle_middle_bits(9) == 15
"""
from typing import Union

def toggle_middle_bits(n: int):
    output = n & (~0b1) | (n ^ (~0b1))
    
    return output