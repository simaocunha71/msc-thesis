def max_sum_increasing_subseq(nums: list, k: int, i: int, n: int) -> int:
  if i < 0 or k < 0 or k < i or k >= n:
    return 0
  return nums[i] + max(max_sum_increasing_subseq(nums, k, i-1, n), max_sum_increasing_subseq(nums, k-1, i-1, n))