def left_insertion(nums, val):
    try:
        return nums.index(val)
    except ValueError:
        for i in range(len(nums)):
            if nums[i] > val:
                return i
        return len(nums) - 1