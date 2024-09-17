def max_sum_increasing_subseq(nums:list,n:int,i:int,k:int) -> int:
  if k < n:
    return 0
  dp = [0 for _ in range(n)]
  for i in range(n):
    if i == 0:
      dp[i] = nums[i]
    else:
      dp[i] = max(dp[i-1], dp[i] + nums[i])
  return dp[k-1]