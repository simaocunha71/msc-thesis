def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = matrix[i][i]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            if matrix[i][j] > dp[i][j]:
                dp[i][j] = matrix[i][j]

    return sum(dp[0]) / (n * n)