
def maxAverageOfPath(matrix):
    dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    dp[-1][-1] = matrix[-1][-1]
    for i in reversed(range(len(matrix)-1)):
        dp[i][-1] = dp[i+1][-1] + matrix[i][-1]
    for i in reversed(range(len(matrix[0])-1)):
        dp[-1][i] = dp[-1][i+1] + matrix[-1][i]
    for i in reversed(range(len(matrix)-1)):
        for j in reversed(range(len(matrix[0])-1)):
            dp[i][j] = max(dp[i+1][j] + matrix[i][j], dp[i][j+1] + matrix[i][j])
    return dp[0][0] / (len(matrix) + len(matrix[0]) - 1)


