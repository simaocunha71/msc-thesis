def max_sum(arr: list) -> int:
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    max_sum = dp[0]
    for i in range(1, len(dp)):
        max_sum = max(max_sum, dp[i])
    return max_sum

