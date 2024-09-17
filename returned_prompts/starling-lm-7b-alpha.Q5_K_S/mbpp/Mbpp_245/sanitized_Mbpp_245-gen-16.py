def max_sum(arr):
  dp = [0] * len(arr)
  for i in range(len(arr)):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])
  return dp[-1]