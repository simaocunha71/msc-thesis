def max_subarray_product(nums):
    curr_max = nums[0]
    global_max = nums[0]
    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max * nums[i])
        global_max = max(global_max, curr_max)
    return global_max