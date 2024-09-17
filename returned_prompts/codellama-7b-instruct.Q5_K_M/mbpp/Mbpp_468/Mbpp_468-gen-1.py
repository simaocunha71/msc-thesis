
def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)
    if n == 3:
        return max(arr)

    dp = [0] * (n + 1)

    dp[1] = arr[0]
    dp[2] = max(arr[0], arr[1])
    dp[3] = max(arr[0], arr[2])
    dp[4] = max(arr[0], arr[3])

    for i in range(4, n):
        dp[i] = max(dp[i - 1], dp[i - 2] * arr[i], dp[i - 3] * arr[i])

    return dp[n - 1]


