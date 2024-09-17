
def max_sum_increasing_subseq(arr: list, n: int, i: int, k: int) -> int:
  dp = [0]*n
  dp[i] = arr[i]
  for j in range(i+1, k+1):
    dp[j] = max(dp[j], arr[j])
    for x in range(i, j):
      if arr[x] < arr[j]:
        dp[j] = max(dp[j], dp[x]+arr[j])
  return max(dp)


