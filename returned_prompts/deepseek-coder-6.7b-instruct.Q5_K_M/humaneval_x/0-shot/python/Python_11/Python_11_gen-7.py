from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010',  '110')
    '100'
    """
    # XOR operation on two binary strings
    xor_result = [str(int(a[i]) ^ int(b[i])) for i in range(len(a))]
    return ''.join(xor_result)


print(string_xor('010', '110'))  # Output: '100'

In this solution, we convert each character of the input strings into an integer, perform the XOR operation, and then convert the result back into a string. The XOR operation is performed on each corresponding character of the input strings.

The time complexity of this solution is O(n), where n is the length of the input strings. The space complexity is also O(n), as we are creating a new list to store the XOR operation results.

This solution assumes that the input strings a and b are of the same length. If they can have different lengths, you would need to pad the shorter string with leading zeros before performing the XOR operation.
