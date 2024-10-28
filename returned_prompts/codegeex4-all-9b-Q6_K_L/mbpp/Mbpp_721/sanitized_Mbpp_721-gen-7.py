def maxAverageOfPath(matrix):
    # Initialize the dp array with -inf
    dp = [[float('-inf')] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
    dp[0][0] = 0
    
    # Traverse the matrix
    for i in range(1, len(matrix) + 1):
        for j in range(1, len(matrix[0]) + 1):
            # Calculate the maximum average path
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i-1][j-1]
    
    # Calculate the total cost and number of cells visited
    total_cost = dp[-1][-1]
    num_cells = len(matrix) * len(matrix[0])
    
    # Return the maximum average path
    return total_cost / num_cells