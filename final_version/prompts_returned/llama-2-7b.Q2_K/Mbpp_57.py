"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
import math

def find_Max_Num(nums):
   n = len(nums)
   max1 = 0

   # For each digit:
   for i in range(n):
      # For each position (i + 1 to N - 1):
      for j in range(n):
         # If the current position is larger than the largest one seen so far, we can stop.
         if j == n-2 and nums[j] > max1:
            max1 = nums[i + j + 1]
   return max1