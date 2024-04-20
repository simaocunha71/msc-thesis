"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
from typing import List, Tuple


class Solution:
    def removeKChar(self, str: str, k: int) -> str:
        """
            :type str: str
            :type k: int
            :rtype: str
        """
        return self.odd_values_string(str)

    def odd_values_string(self, str: str) -> str:
        """
            :param str: input string
        """
        result = ''
        for i in range(len(str)):
            if (i + 1) % k == 1:
                break
            else:
                result += str[i]
        return result
