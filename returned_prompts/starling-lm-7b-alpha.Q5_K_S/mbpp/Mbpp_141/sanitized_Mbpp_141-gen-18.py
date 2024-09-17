def pancake_sort(nums):
    for i in range(len(nums) // 2):
        max_index = nums.index(max(nums[:len(nums) - i]))
        nums.insert(0, nums[max_index])
        nums.pop(max_index + i)
    return nums