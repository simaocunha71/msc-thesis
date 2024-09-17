def zero_count(nums):
    if len(nums) == 0:
        return 0
    zero_count = nums.count(0)
    non_zero_count = len(nums) - zero_count
    return zero_count/non_zero_count