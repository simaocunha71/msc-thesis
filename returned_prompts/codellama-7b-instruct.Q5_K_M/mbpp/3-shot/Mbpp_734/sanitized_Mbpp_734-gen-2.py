def sum_Of_Subarray_Prod(arr):
  n = len(arr)
  dp = [1] * (n + 1)

  for i in range(1, n + 1):
    for j in range(1, i + 1):
      dp[i] += dp[i - j] * arr[i - j]

  return dp[n]