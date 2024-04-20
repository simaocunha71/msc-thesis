"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""
import math
from typing import Optional, Union

def find_parity_int(n: int) -> bool:
    return n%2
    
def find_parity(n: float) -> bool:
    assert isinstance(n, Union[float, int])
    """Write a python function to check if the parity of given input is odd.
    :param n: The value on which you have to calculate parity.
    :return: True if the n's parity is odd else False.
    
    Examples:
        # Call find_parity(12) and find out whether 12 is odd or even.
        assert find_parity(12) == False
    """
    return int(math.fsum(find_parity_int(n), n))%2 != 0