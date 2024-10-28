def max_sum_increasing_subseq(nums, i, k, n):
    if i >= n or k > n:
        return 0
    if i == 0:
        return nums[i]
    max_sum = 0
    for j in range(i):
        if nums[j] < nums[i]:
            max_sum = max(max_sum, max_sum_increasing_subseq(nums, j, k, n) + nums[i])
    max_sum = max(max_sum, max_sum_increasing_subseq(nums, i+1, k, n))
    return max_sum