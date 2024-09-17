def max_sum_increasing_subseq(nums: list, k: int, i: int, n: int) -> int:
  max_sum = 0
  for j in range(i, k):
    max_sum += nums[j]
  return max_sum