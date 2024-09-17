def max_sum(nums: list) -> int:
  n = len(nums)
  dp = [0 for _ in range(n+1)]
  for i in range(n):
    dp[i+1] = max(dp[i], dp[i+1]) + nums[i]
  return dp[n]