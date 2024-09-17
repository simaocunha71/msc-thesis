def max_sum_increasing_subseq(nums: list, i: int, k: int, n: int) -> int:
  dp = [0]*n
  dp[0] = nums[0]
  for j in range(1,n):
    if j > k:
      dp[j] = dp[j-1]
    else:
      dp[j] = max(nums[j] + dp[j-1], dp[j-1])
  return dp[i]