def check_Consecutive(nums: list) -> bool:
    return len(nums) == len(set(nums)) and max(nums) == len(nums) and min(nums) == 1