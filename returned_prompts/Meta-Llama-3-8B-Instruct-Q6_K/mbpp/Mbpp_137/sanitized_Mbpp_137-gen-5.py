import math
def zero_count(nums):
  zeroes = sum(1 for num in nums if num == 0)
  non_zeroes = len(nums) - zeroes
  return zeroes / non_zeroes if non_zeroes else 0