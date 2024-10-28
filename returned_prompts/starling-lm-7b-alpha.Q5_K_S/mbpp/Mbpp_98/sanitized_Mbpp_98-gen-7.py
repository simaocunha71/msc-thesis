import math
def multiply_num(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod / len(nums)