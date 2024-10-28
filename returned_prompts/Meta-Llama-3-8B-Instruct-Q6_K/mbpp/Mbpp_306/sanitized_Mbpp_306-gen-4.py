def max_sum_increasing_subseq(nums, i, k, prefix_sum):
    if i >= k:
        return prefix_sum[i]
    else:
        return max(max_sum_increasing_subseq(nums, i+1, k, prefix_sum), prefix_sum[i] + nums[k] - nums[i-1])