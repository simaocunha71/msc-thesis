def maxAverageOfPath(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = matrix[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
    return dp[m - 1][n - 1] / (m + n - 1)


matrix = [[1, 2, 3], [6, 5, 4], [7, 3, 9]]
print(maxAverageOfPath(matrix))


matrix = [[1, 2], [3, 4]]
print(maxAverageOfPath(matrix))

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(maxAverageOfPath(matrix))















"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.

Ex)

assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2



The function should return the