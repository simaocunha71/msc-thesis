
def max_sum_increasing_subseq(nums: list, n: int, k: int, i: int) -> int:
  dp = [0]*n
  dp[i] = nums[i]
  for j in range(i+1, n):
    if nums[j] > nums[i]:
      dp[j] = max(dp[j], dp[i] + nums[j])
      i = j
  return dp[k]


