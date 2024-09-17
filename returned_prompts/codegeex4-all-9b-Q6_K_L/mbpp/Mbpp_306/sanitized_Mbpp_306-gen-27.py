def max_sum_increasing_subseq(nums: list, length: int, k: int, i: int) -> int:
  if k <= i or i >= length:
    return 0
  sum = 0
  for j in range(i+1, k+1):
    sum += nums[j]
  return sum