
def max_sum_increasing_subseq(nums: list, i: int, k: int, n: int) -> int:
  dp = [0 for _ in range(n)]
  dp[i] = nums[i]
  for j in range(i + 1, k):
    dp[j] = max(dp[j-1], nums[j])
  return dp[k-1]


