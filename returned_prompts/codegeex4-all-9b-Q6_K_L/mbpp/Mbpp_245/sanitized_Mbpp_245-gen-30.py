def max_sum(nums: list) -> int:
  dp = [0]*len(nums)
  dp[0] = nums[0]
  dp[-1] = nums[-1]
  for i in range(1, len(nums)):
    dp[i] = max(dp[i-1]+nums[i], nums[i])
  for i in range(len(nums)-2, -1, -1):
    dp[i] = max(dp[i+1]+nums[i], dp[i])
  return max(dp)