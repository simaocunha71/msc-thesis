import math
def unique_product(nums):
  return math.prod(set(nums)) if nums else 1