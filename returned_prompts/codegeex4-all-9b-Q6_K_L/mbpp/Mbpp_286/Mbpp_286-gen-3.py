def max_sub_array_sum_repeated(nums: list, k: int, n: int) -> int:
  window_sum = sum(nums[:n])
  max_sum = window_sum
  for i in range(1, k):
    window_sum = window_sum - nums[i-1] + nums[i*n-1]
    max_sum = max(max_sum, window_sum)
  return max_sum