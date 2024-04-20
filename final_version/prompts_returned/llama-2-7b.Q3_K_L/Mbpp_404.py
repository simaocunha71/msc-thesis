"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""
class Solution:
    def minimum(self, num1: int, num2: int) -> int:
        return max(0, num1 - num2) if num2 < num1 else max(num2 - 0, num2 - num1)