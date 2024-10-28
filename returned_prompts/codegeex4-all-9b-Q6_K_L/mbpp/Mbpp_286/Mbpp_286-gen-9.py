def max_sub_array_sum_repeated(nums: list, k: int, size: int) -> int:
  # Initialize variables
  window_sum = 0
  max_sum = float('-inf')
  for i in range(size):
    window_sum += nums[i]
  max_sum = max(max_sum, window_sum)
  for i in range(size, len(nums)):
    window_sum += nums[i] - nums[i - size]
    max_sum = max(max_sum, window_sum)
  # Repeat the process for k times
  for i in range(1, k):
    window_sum += nums[i * size - size : i * size]
    max_sum = max(max_sum, window_sum)
  return max_sum

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))