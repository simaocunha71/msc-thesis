from functools import reduce
from itertools import product
from operator import mul
from math import prod
def multiply_num(nums):
  return reduce(mul, nums, 1) / len(nums)