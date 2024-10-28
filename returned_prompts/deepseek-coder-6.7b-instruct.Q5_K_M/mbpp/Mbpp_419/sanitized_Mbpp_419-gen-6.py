def round_and_sum(nums):
    return sum(round(n) for n in nums) * len(nums)