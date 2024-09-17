def largest_subset(nums: list):
  nums.sort()
  dp = [1] * len(nums)
  for i in range(1, len(nums)):
    for j in range(i):
      if nums[i] % nums[j] == 0:
        dp[i] = max(dp[i], dp[j] + 1)
  return max(dp)