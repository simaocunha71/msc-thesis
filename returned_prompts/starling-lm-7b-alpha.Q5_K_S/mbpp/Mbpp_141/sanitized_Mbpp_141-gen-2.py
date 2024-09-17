def pancake_sort(nums):
    while len(nums) > 1:
        max_num = max(nums[:-1])
        idx = nums.index(max_num)
        nums.insert(0, nums.pop(idx))
    return nums