from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    return result


# Test the function
print(string_xor('010', '110'))  # Output: 100
print(string_xor('111', '000'))  # Output: 111
print(string_xor('1001', '1100'))  # Output: 0101
print(string_xor('0000', '0000'))  # Output: 0000
print(string_xor('1111', '1111'))  # Output: 0000
print(string_xor('1010', '0101'))  # Output: 1111
print(string_xor('1101', '1010'))  # Output: 0111
print(string_xor('1110', '1101'))  # Output: 0011
print(string_xor('0001', '1110'))  # Output: 1111
print(string_xor('0101', '1010'))  # Output: 1111
print(string_xor('1111', '0000'))  # Output: 1111
print(string_xor('0000', '1111'))  # Output: 1111
print(string_xor('1010', '1010'))  # Output: 0000
print(string_xor('1101', '1101'))  # Output: 0000
print(string_xor('1111', '1111'))  # Output: 0000
print(string_xor('1010', '1101'))  # Output: 0111
print(string_xor('1101', '1010'))  # Output: 0111
print(string_xor('1110', '1101'))  # Output: 0011
print(string_xor('0001', '1110'))  # Output: 1111
print(string_xor('0101', '1010'))  # Output: 1111
print(string_xor('1111', '0000'))  # Output: 1111
