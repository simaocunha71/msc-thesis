def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i-1][j-1]
    total = dp[n][n]
    path = []
    i, j = n, n
    while i > 0 and j > 0:
        path.append(matrix[i-1][j-1])
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    path.reverse()
    return (total / len(path))

