def round_and_sum(nums: list) -> int:
    return sum(round(num) for num in nums) * len(nums)