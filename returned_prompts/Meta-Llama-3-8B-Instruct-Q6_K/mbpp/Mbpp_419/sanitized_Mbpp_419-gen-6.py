import math
def round_and_sum(nums):
  nums = [round(num) for num in nums]
  total_sum = sum(nums)
  return total_sum * len(nums)