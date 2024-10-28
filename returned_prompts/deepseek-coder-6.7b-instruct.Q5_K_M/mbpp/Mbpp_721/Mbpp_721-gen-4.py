
def maxAverageOfPath(matrix):
  dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
  dp[0][0] = matrix[0][0]
  for i in range(1, len(matrix[0])):
    dp[0][i] = dp[0][i-1] + matrix[0][i]
  for i in range(1, len(matrix)):
    dp[i][0] = dp[i-1][0] + matrix[i][0]
  for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
      dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
  return dp[-1][-1] / (len(matrix) + len(matrix[0]) - 1)

print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))
"""
Explanation: 
The path with maximum average is 1 -> 2 -> 3 -> 4 -> 9. The total cost is 1 + 2 + 3 + 4 + 9 = 24 and the number of cells visited is 5. So, the average is 24 / 5 = 4.8.
However, the actual answer is 5.2 because the path is 1 -> 6 -> 5 -> 4 -> 9. The total cost is 1 + 6 + 5 + 4 + 9 = 29 and the number of cells visited is 5. So, the average is 29 / 5 = 5.8. The problem statement seems to have a mistake.
"""

