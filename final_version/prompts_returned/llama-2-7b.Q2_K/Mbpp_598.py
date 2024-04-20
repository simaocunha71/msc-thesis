"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
class Solution:
    def isArmstrong(self, num):
        """
        :type num: int
        :rtype: bool
        """
       ans = 0
       for digit in str(num):
           cur_val = int(digit)**3
           if cur_val >= ans and cur_val != ans:
               ans += (cur_val -1)/2
       if num == ans: return True else: return False