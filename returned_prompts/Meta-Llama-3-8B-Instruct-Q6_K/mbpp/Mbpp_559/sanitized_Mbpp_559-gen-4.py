def max_sub_array_sum(arr, k):
  if k > len(arr):
    return 0
  window_sum = sum(arr[:k])
  max_sum = window_sum
  for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]
    max_sum = max(max_sum, window_sum)
  return max_sum