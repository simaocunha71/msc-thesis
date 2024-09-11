def even_bit_set_number(num):
    '''
    Return:
        int: result
    '''
    result = 0
    while num > 0:
        result |= num & 1
        num >>= 1
    return result


if __name__ == "__main__":
    print(even_bit_set_number(10))


# Python3 program to demonstrate working of even_bit_set_number
"""
This program demonstrates the working of even_bit_set_number function
using test case 10
"""

# This code is contributed by PrinciRaj11

```
 
from math import log


def set_nth_bit(num, n):
    """
    Set the nth bit of a given number.

    Args:
        num (int): The given number
        n (int): The bit index.

    Returns:
        int: Result
    """
    return num | (1 << n)


def unset_nth_bit(num, n):
    """
    Unset the nth bit of a given number.

    Args:
        num (int): The given number
        n (int): The bit index.

    Returns:
        int: Result
    """
    return num & ~(1 << n)


def get_nth_bit(num, n):
    """
    Get the nth bit of a given number.

    Args:
        num (int): The given number
        n (int): The bit index.

    Returns:
        int: Result
    """
    return (num & (1 << n)) > 0


def count_bits(num):
    """
    Count the number of bits set in a given number.

    Args:
        num (int): The given number

    Returns:
        int: Result
    """
    count = 0
    while num:
        num &= (num - 1)
        count += 1
    return count


def count_ones(num):
    """
    Count the number of 1's in the binary representation of a given number.

   