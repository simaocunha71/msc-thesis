"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""
class Solution:
    def isOdd(self, s):
        """
        :param s: a string contain odd numbers
        :return: True if the nums in string are evenly, False otherwise
        :rtype: bool
        """
        return (not any([int(x) for x in s]))
        