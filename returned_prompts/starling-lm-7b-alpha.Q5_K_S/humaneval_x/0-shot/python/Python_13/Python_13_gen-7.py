

def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# Importing fractions module to use gcd method
from fractions import gcd


def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b """
    return gcd(a, b)


# Testing the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    while b != 0:
        a, b = b, a % b
    return a


# Testing the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b != 0:
        a, b = b, a % b
    return a


# Testing the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5


def greatest_common