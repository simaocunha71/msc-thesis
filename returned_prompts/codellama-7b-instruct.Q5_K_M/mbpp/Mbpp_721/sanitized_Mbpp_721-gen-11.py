def maxAverageOfPath(matrix: list) -> float:
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    ans = 0
    for i in range(rows):
        for j in range(cols):
            if i == rows-1 and j == cols-1:
                ans = max(ans, dp[i][j])
            elif i == rows-1:
                ans = max(ans, dp[i][j] + dp[i][j-1])
            elif j == cols-1:
                ans = max(ans, dp[i][j] + dp[i-1][j])
            else:
                ans = max(ans, dp[i][j] + max(dp[i-1][j], dp[i][j-1]))

    return ans / (rows * cols)