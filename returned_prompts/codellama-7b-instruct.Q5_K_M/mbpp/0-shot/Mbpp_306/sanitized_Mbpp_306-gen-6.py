def max_sum_increasing_subseq(nums, k, i, j):
    if i == j:
        return nums[i]
    else:
        return max(nums[i] + max_sum_increasing_subseq(nums, k, i+1, j),
                   max_sum_increasing_subseq(nums, k, i+1, j))