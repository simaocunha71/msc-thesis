import math
def round_and_sum(nums):
    rounded_nums = [round(num) for num in nums]
    total_sum = sum(rounded_nums)
    return total_sum * len(nums)