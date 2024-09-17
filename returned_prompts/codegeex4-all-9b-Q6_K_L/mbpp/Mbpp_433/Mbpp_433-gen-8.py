def check_greater(nums: list, num: int) -> bool:
    return not all(i < num for i in nums)