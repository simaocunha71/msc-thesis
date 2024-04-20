"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
from typing import Optional, Union

def even_bit_set_number(number: Union[int, float], bits: int = 8):
    """Set all even-bits in a given number

    Args:
        number (int or float): The number to operate on.
        bits (int, optional): Number of bits (1..32) from the right to set. Defaults to 8.

    Returns:
        int | float: number with all even-bits set
    """
    if not isinstance(number, Union[int, float]):
        raise TypeError("Type must be int or float")
    
    if not isinstance(bits, int) or bits < 1 or bits > 32:
        raise ValueError('bits must be a number between 1 and 32')

    number_int = int(number)
    mask = (1 << bits) - 1   # Mask (all ones) with given number of bits.
    
    return number_int & ((~mask) | (number_int ^ mask))