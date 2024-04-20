"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""
from typing import Optional

def left_rotate(num: int, shift_bits : int):
    """
    Implement the rotate function such that a number of d bits in the left is rotated by num to the right.
    
    >>> left_rotate(16,2) == 64
        """
    # print(num & (0xFFFFFFFF >> shift_bits))
    #print(">>> ",end="")
    return(int((num << shift_bits)& (0xFFFFFFFF ^ num)))

def right_rotate(num: int, shift_bits : int):
    """
    Implement the rotate function such that a number of d bits in the right is rotated by num to the left.
    
    >>> left_rotate(16,2) == 64
        """
    # print(num & (0xFFFFFFFF >> shift_bits))
    return((int((num << shift_bits)& (0xFF ^ (-num))))<<shift_bits)