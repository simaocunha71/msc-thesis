from functools import reduce
from operator import mul


def decimal_to_binary(n):
    return bin(n)[2:]


def decimal_to_binary_with_no_leading_zeros(n):
    binary = bin(n)[2:]
    if '0b' in binary:
        binary = binary[2:]
    return binary


def decimal_to_binary_with_no_leading_zeros_v2(n):
    return bin(n)[2:].lstrip('0')


def decimal_to_binary_with_no_leading_zeros_v3(n):
    return '{0:b}'.format(n)[2:]

def decimal_to_binary_with_no_leading_zeros_v4(n):
    """
    >>> decimal_to_binary_with_no_leading_zeros_v4(8)
    '1000'
    """
    binary = bin(n)[2:]
    if '0b' in binary:
        binary = binary[2:]
    return binary

def decimal_to_binary_with_no_leading_zeros_v5(n):
    binary = bin(n)[2:]
    return binary if '0b' not in binary else binary[2:]

def decimal_to_binary_with_no_leading_zeros_v6(n):
    return '{0:b}'.format(n)[2:]

def decimal_to_binary_with_no_leading_zeros_v7(n):
    """
    >>> decimal_to_binary_with_no_leading_zeros_v7(8)
    '1000'
    """
    return '{0:b}'.format(n)[2:]

if __name__ == '__main__':
    print(decimal_to_binary(8))
    print(decimal_to_binary_with_no_leading_zeros(8))
    print(decimal_to_binary_with_no_leading_zeros_v2(8))
    print(decimal_to_binary_with