
def maxAverageOfPath(matrix):
  m = len(matrix)
  n = len(matrix[0])
  dp = [[0 for i in range(n)] for j in range(m)]
  dp[0][0] = matrix[0][0]
  for i in range(m):
    for j in range(n):
      if i == 0 and j == 0:
        continue
      if i != 0:
        dp[i][j] = max(dp[i][j], dp[i-1][j] + matrix[i][j])
      if j != 0:
        dp[i][j] = max(dp[i][j], dp[i][j-1] + matrix[i][j])
  return dp[m-1][n-1]/2


