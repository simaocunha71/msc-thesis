def is_Monotonic(nums):
    is_non_increasing = True
    is_non_decreasing = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            is_non_decreasing = False
        if nums[i] < nums[i - 1]:
            is_non_increasing = False
    return is_non_decreasing or is_non_increasing