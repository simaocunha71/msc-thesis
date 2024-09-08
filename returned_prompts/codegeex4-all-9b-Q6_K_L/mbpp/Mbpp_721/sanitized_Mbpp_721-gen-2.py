def maxAverageOfPath(matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first cell
    dp[0][0] = matrix[0][0]

    # Initialize the first row
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + matrix[0][i]

    # Initialize the first column
    for j in range(1, n):
        dp[j][0] = dp[j-1][0] + matrix[j][0]

    # Fill the rest of the dp table
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    # Calculate the maximum average
    max_avg = 0
    for i in range(n):
        for j in range(n):
            total_cost = dp[i][j]
            cells_visited = (i + 1) * (j + 1)
            max_avg = max(max_avg, total_cost / cells_visited)

    return max_avg