def consecutive_duplicates(nums: list) -> list:
    return [num for i, num in enumerate(nums) if i == 0 or num != nums[i - 1]]