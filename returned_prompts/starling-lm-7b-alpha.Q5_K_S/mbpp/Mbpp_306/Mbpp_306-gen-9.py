def max_sum_increasing_subseq(arr, i, k, n):
    dp = [0] * n
    for idx, val in enumerate(arr):
        if idx <= i:
            dp[idx] = val
        else:
            dp[idx] = max(dp[idx - 1], dp[idx])

    for idx, val in enumerate(arr):
        if idx >= k:
            dp[idx] = max(dp[idx - 1], dp[idx] + val)
    return dp[n - 1]

# Test
print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11)
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 2, 6, 15) == 38)
print(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,