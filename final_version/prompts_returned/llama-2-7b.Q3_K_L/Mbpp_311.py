"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
class Solution:
    def setLeftMostBit(self, n):
        return (1<<n)+1