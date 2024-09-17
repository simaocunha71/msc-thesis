def pos_count(nums: list) -> int:
    return sum(1 for num in nums if num > 0)