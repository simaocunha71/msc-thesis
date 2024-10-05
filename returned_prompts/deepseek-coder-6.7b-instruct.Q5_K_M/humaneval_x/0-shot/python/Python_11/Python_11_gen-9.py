from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


print(string_xor('010', '110'))  # Output: '100'

Explanation:
The function string_xor takes two binary strings a and b as input. It initializes an empty string result. It then loops through the elements in a and b in parallel. If the i-th element in a and b is the same, it appends '0' to result. If the i-th element in a and b is different, it appends '1' to result. The function returns the resulting string.
"""

#tests/test_binary_xor.py
import unittest
from binary_xor import string_xor


class BinaryXorTest(unittest.TestCase):

    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '110'), '011')
        self.assertEqual(string_xor('111', '111'), '111')
        self.assertEqual(string_xor('000', '000'), '000')
        self.assertEqual(string_xor('10101010', '01010101'), '11111111')


if __name__ == "__main__":
    unittest.main()#scripts/utils.py
def get_input(day: int, is_test: bool = False