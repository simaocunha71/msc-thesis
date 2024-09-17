def move_zero(nums):
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[i+zero_count] = nums[i+zero_count], nums[i]
    return nums