def maxAverageOfPath(arr: list, n: int) -> float:
    dp = [[0 for _ in range(n)] for _ in range(n)]
    max_avg = 0
    for i in range(n):
        for j in range(n):
            if i == j == 0:
                dp[i][j] = arr[i][j]
            elif i == 0:
                dp[i][j] = max(dp[i][j-1], arr[i][j])
            elif j == 0:
                dp[i][j] = max(dp[i-1][j], arr[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], arr[i][j])
            if i == n - 1 and j == n - 1:
                max_avg = max(max_avg, dp[i][j])
    return max_avg / (n * n)