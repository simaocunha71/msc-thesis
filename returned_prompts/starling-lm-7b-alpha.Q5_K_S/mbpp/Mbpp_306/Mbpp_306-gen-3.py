
def max_sum_increasing_subseq(nums: list, i: int, k: int, n: int) -> int:
  prefix_sums = [0] * (n + 1)
  suffix_sums = [0] * (n + 1)
  for i in range(1, n + 1):
    if i > 1:
      prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
    if i < n:
      suffix_sums[i] = suffix_sums[i - 1] + nums[n - i]
  return prefix_sums[i] + suffix_sums[k] - nums[i - 1]


