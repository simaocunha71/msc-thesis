"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
from typing import Optional

def decimal_to_binary(decimal: int = 99) -> str:
    """Convert the given integer to its binary equivalent in a single line of code, represented as a string with no leading zeros.
    
    Args:
        decimal (int): The number to be converted into binary format.
        
    Raises:
        ValueError: If `decimal` is less than 0 or greater than 256.
                    Note that in order to avoid overflowing, the maximum value of int on Python 3 is limited to 2 ** 31 - 1 (2,147,483,647). 
        
        TypeError: If `decimal` is not an integer.
    
    Returns:
        str: The binary equivalent of the given decimal number.
    """
    if decimal < 0 or decimal > int(pow(2, 31) - 1):
        raise ValueError('The value must be between (0 <= value <= {})'.format(int(pow(2, 31) - 1)))
    
    binary = ''
    if not isinstance(decimal, int):
        raise TypeError('`decimal_to_binary()` expects int arguments')
    while decimal > 0:
        binary += '{:08b}'.format(bin(decimal)[2:])   # Convert to binary and use [2:] to omit the leading "1"
        decimal = (decimal - bin(decimal)[3] * int('{0:b}{1:b}'.format(decimal, binary[-1]))) % 2 ** 8
    return binary.rstrip()