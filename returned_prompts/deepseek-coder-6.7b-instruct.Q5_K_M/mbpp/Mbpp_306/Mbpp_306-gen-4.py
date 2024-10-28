
def max_sum_increasing_subseq(arr, n, k, i):
  dp = [0]*n
  dp[i] = arr[i]
  max_sum = dp[i]
  for j in range(i+1, n):
    if arr[j] > arr[i]:
      dp[j] = max(dp[j], dp[i] + arr[j])
      max_sum = max(max_sum, dp[j])
  for j in range(i-1, -1, -1):
    if arr[j] < arr[k]:
      dp[j] = max(dp[j], dp[k] + arr[j])
      max_sum = max(max_sum, dp[j])
  return max_sum

