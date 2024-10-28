def max_sub_array_sum(nums, n):
    if n < 1:
        return 0
    max_sum = curr_sum = nums[0]
    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum