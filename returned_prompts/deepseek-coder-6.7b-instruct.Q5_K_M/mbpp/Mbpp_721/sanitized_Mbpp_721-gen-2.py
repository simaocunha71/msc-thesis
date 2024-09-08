def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = matrix[0][0] / 2.0
    
    # Initialize first row
    for j in range(1, N):
        dp[0][j] = max(dp[0][j-1], matrix[0][j] / 2.0) + matrix[0][j] / 2.0

    # Initialize first column
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0], matrix[i][0] / 2.0) + matrix[i][0] / 2.0

    # Fill in the rest of the dp table
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], matrix[i][j] / 2.0) + matrix[i][j] / 2.0

    return dp[-1][-1]