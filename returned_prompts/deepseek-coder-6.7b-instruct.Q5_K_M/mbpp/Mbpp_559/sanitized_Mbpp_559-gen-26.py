def max_sub_array_sum(nums, n):
    max_sum = 0
    curr_sum = 0
    for i in range(0, n):
        curr_sum += nums[i]
    max_sum = curr_sum
    for i in range(n, len(nums)):
        curr_sum = curr_sum - nums[i-n] + nums[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum