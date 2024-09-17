def nth_nums(nums, n):
    for i in range(len(nums)):
        nums[i] = nums[i] ** n
    return nums