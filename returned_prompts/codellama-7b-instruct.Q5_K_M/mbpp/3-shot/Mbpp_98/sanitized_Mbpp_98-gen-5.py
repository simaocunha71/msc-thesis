from functools import reduce
from typing import List
from math import prod
def multiply_num(nums: List) -> float:
    return prod(nums) / len(nums)