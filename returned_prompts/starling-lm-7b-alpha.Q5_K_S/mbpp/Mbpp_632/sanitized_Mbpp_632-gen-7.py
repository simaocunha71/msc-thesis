def move_zero(nums):
    zero_index = len(nums) - 1
    while zero_index >= 0:
        if nums[zero_index] != 0:
            nums[zero_index], nums[zero_index - 1] = nums[zero_index - 1], nums[zero_index]
            zero_index -= 1
        else:
            zero_index -= 1
    return nums