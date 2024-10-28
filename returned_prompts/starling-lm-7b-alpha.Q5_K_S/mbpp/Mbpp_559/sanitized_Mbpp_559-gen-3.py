def max_sub_array_sum(nums, k):
    # Write Your Code here
    max_sum = 0
    for i in range(len(nums)-k+1):
        curr_sum = 0
        for j in range(k):
            curr_sum += nums[i+j]
        max_sum = max(max_sum, curr_sum)
    return max_sum