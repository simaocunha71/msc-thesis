import math
def multiply_num(nums: tuple) -> float:
  product = 1
  for num in nums:
    product *= num
  return product/len(nums)