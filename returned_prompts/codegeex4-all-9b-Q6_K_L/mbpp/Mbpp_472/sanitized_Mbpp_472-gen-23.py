def check_Consecutive(nums: list) -> bool:
    return sorted(nums) == list(range(min(nums), max(nums)+1))