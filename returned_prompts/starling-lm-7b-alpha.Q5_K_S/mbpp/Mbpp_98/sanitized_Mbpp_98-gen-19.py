import math
def multiply_num(nums: tuple) -> float:
  product = 1
  for i in nums:
    product *= i
  return product / len(nums)