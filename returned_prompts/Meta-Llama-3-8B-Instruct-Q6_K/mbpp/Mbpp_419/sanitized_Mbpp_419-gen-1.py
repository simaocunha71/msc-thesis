import math
def round_and_sum(nums):
    rounded_nums = [math.floor(num) if num < 0 else math.ceil(num) for num in nums]
    return sum(rounded_nums) * len(nums)  # or sum(rounded_nums) * len(nums) if you want to avoid division by zero