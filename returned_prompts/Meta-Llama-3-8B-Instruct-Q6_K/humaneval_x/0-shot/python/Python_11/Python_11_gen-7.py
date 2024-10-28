from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    return ''.join('1' if a[i] != b[i] else '0' for i in range(len(a)))
    # ^ is the XOR operator. It returns 1 if the bits are different, 0 if they are the same.
    # It is used to XOR two binary numbers. In Python, you can use it with the ^ operator.
    # For example, 1 ^ 1 is 0 and 1 ^ 0 is 1.
    # This function works by iterating over the input strings, performing XOR on each pair of bits,
    # and then joining the results together into a single string.
    # The result is a string that is the XOR of the input strings.
    # For example, string_xor('010', '110') returns '100', which is the XOR of the two input strings.