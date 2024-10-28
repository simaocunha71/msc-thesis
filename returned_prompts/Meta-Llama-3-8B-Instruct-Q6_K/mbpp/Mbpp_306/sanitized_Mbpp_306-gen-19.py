def max_sum_increasing_subseq(arr, i, k, j):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for idx in range(n + 1):
        dp[idx][0] = 0
    for idx in range(1, n + 1):
        for jdx in range(1, min(idx + 1, k + 1)):
            if jdx == 1:
                dp[idx][jdx] = dp[idx - 1][jdx]
            else:
                dp[idx][jdx] = max(dp[idx - 1][jdx], dp[idx - 1][jdx - 1] + arr[idx - 1])
    return dp[n][k]