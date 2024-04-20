"""
Write a python function to check whether the given number is even or not.
assert is_Even(1) == False
"""
class Solution:
    def is_Even(self, num):
        if (num % 2==0):
            return True
        else:
            return False