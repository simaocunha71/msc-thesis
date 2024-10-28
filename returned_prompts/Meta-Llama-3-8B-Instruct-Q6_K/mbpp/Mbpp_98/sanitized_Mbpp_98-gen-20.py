import math
def multiply_num(nums):
    product = 1
    for num in nums:
        product *= num
    return product / len(nums)