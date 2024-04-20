"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
class Solution:
    def differ_At_One_Bit_Pos(self, x, y):
        if((x ^ y) & 0X1) != 0X1 :
            return False
        
        return True