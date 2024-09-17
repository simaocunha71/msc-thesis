import math
def multiply_num(nums: list) -> float:
  multiplied_nums = 1
  for num in nums:
    multiplied_nums *= num
  return multiplied_nums / len(nums)