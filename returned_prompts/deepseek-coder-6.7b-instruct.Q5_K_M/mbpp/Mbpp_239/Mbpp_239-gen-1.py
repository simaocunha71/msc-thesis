
def get_total_number_of_sequences(m: int, n: int) -> int:
  dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
  for i in range(1, m+1):
    dp[i][1] = 1
  
  for j in range(2, n+1):
    for i in range(1, m+1):
      for k in range(2*i, min(i+1, m+1)):
        dp[k][j] += dp[i][j-1]
  
  return sum(dp[i][n] for i in range(1, m+1))


