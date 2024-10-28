def last(nums, target):
    for i in reversed(range(len(nums))):
        if nums[i] == target:
            return i
    return -1