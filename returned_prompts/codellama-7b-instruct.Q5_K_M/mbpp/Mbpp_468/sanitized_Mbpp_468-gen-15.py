def max_product(arr):
  n = len(arr)
  if n == 0:
    return 0
  if n == 1:
    return arr[0]

  dp = [0] * n
  dp[0] = arr[0]
  max_product = arr[0]

  for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] * arr[i], arr[i] * dp[i - 1])
    max_product = max(max_product, dp[i])

  return max_product