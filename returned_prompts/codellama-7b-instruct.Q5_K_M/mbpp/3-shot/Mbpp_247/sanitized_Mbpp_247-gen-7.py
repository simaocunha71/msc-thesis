def lps(s: str) -> int:
  n = len(s)
  dp = [0] * (n + 1)
  longest = 0
  for i in range(1, n + 1):
    for j in range(i, 0, -1):
      if s[j - 1] == s[i - 1]:
        dp[i] = max(dp[i], dp[i - j] + 1)
      else:
        break
      if dp[i] > longest:
        longest = dp[i]
  return longest