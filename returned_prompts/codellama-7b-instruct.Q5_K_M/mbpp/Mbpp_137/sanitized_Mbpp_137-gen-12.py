import math
def zero_count(nums: list) -> float:
  count = 0
  for i in nums:
    if i == 0:
      count += 1
  return count / len(nums)