def pancake_sort(nums):
    while nums:
        max_num_index = nums.index(max(nums))
        if max_num_index == len(nums) - 1:
            nums.pop()
        else:
            nums[max_num_index], nums[-1] = nums[-1], nums[max_num_index]
            nums = nums[:max_num_index+1]
    return nums