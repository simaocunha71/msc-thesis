def count_binary_seq(n):
  dp = [0]*(2*n+1)
  dp[0] = dp[1] = 1
  for i in range(2, 2*n+1):
    dp[i] = 0
    for j in range(i-1):
      dp[i] += dp[j]*dp[i-j-1]
  return dp[2*n]