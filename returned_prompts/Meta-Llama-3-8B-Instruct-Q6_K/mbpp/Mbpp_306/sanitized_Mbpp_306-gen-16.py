def max_sum_increasing_subseq(nums, i, k, prefix_sum):
    max_sum = prefix_sum[i]
    for j in range(i, k):
        if nums[j] > nums[j-1]:
            max_sum += nums[j]
    return max_sum