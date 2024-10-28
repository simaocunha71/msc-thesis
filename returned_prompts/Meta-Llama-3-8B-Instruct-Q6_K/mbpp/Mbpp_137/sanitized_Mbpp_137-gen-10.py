import math
def zero_count(nums: list) -> float:
  zero_count = sum(1 for num in nums if num == 0)
  non_zero_count = len(nums) - zero_count
  if non_zero_count == 0:
    return 0
  return zero_count / non_zero_count