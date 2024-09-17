def max_sum_increasing_subseq(nums, n, i, k):
    if k > n:
        return 0
    max_sum = [0] * (n + 1)
    max_sum[0] = 0
    max_sum[1] = 0
    for j in range(1, k + 1):
        max_sum[j] = max_sum[j - 1] + nums[j - 1]
    for j in range(k + 1, n + 1):
        max_sum[j] = max(max_sum[j - 1], nums[j - 1])
        for l in range(k + 1, j):
            if nums[l - 1] <= nums[j - 1]:
                max_sum[j] = max(max_sum[j], max_sum[l] + nums[j - 1])
    return max_sum[n]