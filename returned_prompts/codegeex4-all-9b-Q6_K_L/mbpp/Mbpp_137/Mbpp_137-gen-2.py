def zero_count(nums: list) -> float:
    zero_count = nums.count(0)
    non_zero_count = len(nums) - zero_count
    ratio = zero_count / non_zero_count
    return ratio

