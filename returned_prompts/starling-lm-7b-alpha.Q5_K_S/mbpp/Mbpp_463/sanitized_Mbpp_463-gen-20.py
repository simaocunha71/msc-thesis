def max_subarray_product(nums):
    result = max_so_far = max_ending_here = nums[0]
    for i in range(len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far