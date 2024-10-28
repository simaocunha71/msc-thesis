def max_sum_increasing_subseq(nums, k, i, n):
    if i >= k or k > n or i >= n:
        return 0
    return nums[i] + max(max_sum_increasing_subseq(nums, k, i+1, n),
                          max_sum_increasing_subseq(nums, k+1, i+1, n))

