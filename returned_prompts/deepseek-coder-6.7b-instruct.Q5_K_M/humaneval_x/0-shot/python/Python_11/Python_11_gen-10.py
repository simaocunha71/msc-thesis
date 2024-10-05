from typing import List


def string_xor(a: str, b: str)  -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length")
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


print(string_xor('010', '110'))  # '100'


In this solution, we iterate through each character in the strings and perform an XOR operation on each pair of bits. If the bits are the same, we add a '0' to the result. If the bits are different, we add a '1'. We then return the result as a string.
"""

# 2.
"""
