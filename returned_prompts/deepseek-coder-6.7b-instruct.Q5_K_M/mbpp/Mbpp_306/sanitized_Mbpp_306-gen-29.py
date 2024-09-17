def max_sum_increasing_subseq(arr, n, i, k):
  dp = [0]*n
  dp[i] = arr[i]
  for j in range (i+1, n):
    if arr[j] > arr[i]:
      dp[j] = max(dp[j], dp[i] + arr[j])
      i = j
  dp[k] = max(dp[k], dp[i] + arr[k])
  return max(dp)