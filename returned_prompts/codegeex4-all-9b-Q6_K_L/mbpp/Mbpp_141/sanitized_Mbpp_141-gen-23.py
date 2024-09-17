def pancake_sort(nums: list) -> list:
    for i in range(len(nums)-1, 0, -1):
        max_index = nums.index(max(nums[:i+1]))
        if max_index != i:
            nums[max_index:i+1] = reversed(nums[max_index:i+1])
            nums[:i+1] = reversed(nums[:i+1])
    return nums