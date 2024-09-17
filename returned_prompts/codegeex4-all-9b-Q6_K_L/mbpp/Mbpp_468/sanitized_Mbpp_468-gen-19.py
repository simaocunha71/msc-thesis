def max_product(nums: list) -> int:
  n = len(nums)
  dp = [1] * n
  for i in range(n):
    for j in range(i):
      if nums[i] > nums[j]:
        dp[i] = max(dp[i], dp[j] * nums[i])
  return max(dp)