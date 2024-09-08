def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = matrix[0][0]
    
    # Initialize the first row and the first column
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], matrix[i][0])
        dp[0][i] = max(dp[0][i-1], matrix[0][i])
    
    # Fill in the rest of the dp table
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    # The maximum average path is in the bottom right cell
    return dp[-1][-1] / (n-1)