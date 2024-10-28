def maxAverageOfPath(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = matrix[0][0]
    
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
        
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
    
    return sum(dp[-1]) / (rows * cols)
