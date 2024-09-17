def left_insertion(nums, target):
    index = 0
    while index < len(nums) and nums[index] < target:
        index += 1
    return index