
def count_binary_seq(n):
  dp = [0]*(2*n+1)
  dp[0] = dp[1] = 1
  for i in range(2, 2*n+1):
    for j in range(1, i//2+1):
      dp[i] += dp[j-1]*dp[i-j]
  return dp[2*n]


