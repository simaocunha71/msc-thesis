def move_zero(nums: list) -> list:
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            nums[i - count] = nums[i]
    for i in range(len(nums) - count, len(nums)):
        nums[i] = 0
    return nums