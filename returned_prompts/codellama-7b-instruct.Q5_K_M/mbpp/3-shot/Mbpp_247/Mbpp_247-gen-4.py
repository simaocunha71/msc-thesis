
def lps(s):
  n = len(s)
  dp = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    dp[i][i] = 1

  for i in range(n-1):
    if s[i] == s[i+1]:
      dp[i][i+1] = 2

  for k in range(2,n):
    for i in range(n-k):
      if s[i] == s[i+k]:
        dp[i][i+k] = 2 + dp[i+1][i+k-1]
      else:
        dp[i][i+k] = max(dp[i][i+k-1], dp[i+1][i+k])

  return dp[0][n-1]


