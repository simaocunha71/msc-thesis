from math import ceil
def round_and_sum(nums):
    rounded_nums = [ceil(num) if num < 0 else round(num) for num in nums]
    return sum(rounded_nums) * len(rounded_nums)