def round_and_sum(nums):
    nums = [round(i) for i in nums]
    return sum(nums) * len(nums)