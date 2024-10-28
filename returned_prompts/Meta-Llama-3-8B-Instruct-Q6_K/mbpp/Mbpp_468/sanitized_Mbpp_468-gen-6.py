def max_product(arr):
    max_dp = [0] * len(arr)
    min_dp = [0] * len(arr)
    max_dp[0] = arr[0]
    min_dp[0] = arr[0]
    res = arr[0]
    for i in range(1, len(arr)):
        max_dp[i] = max(arr[i], max_dp[i-1] * arr[i], min_dp[i-1] * arr[i])
        min_dp[i] = min(arr[i], max_dp[i-1] * arr[i], min_dp[i-1] * arr[i])
        res = max(res, max_dp[i])
    return res