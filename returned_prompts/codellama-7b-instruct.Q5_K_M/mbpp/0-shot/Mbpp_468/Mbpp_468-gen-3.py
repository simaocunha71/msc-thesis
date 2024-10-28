"""
def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    if n == 3:
        return max(arr[0] * arr[1] * arr[2], arr[0] * arr[2] * arr[1], arr[1] * arr[0] * arr[2], arr[1] * arr[2] * arr[0], arr[2] * arr[0] * arr[1], arr[2] * arr[1] * arr[0])

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1] * arr[i], arr[i])

        for j in range(i - 2, -1, -1):
            dp[i] = max(dp[i], dp[j] * arr[i])

    return dp[-1]
"""
