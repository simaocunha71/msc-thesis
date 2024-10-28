def max_product(arr):
    if not arr:
        return 0

    dp = [0] * len(arr)
    dp[0] = arr[0]
    max_product = dp[0]

    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i-1] * arr[i])
        max_product = max(max_product, dp[i])

    return max_product