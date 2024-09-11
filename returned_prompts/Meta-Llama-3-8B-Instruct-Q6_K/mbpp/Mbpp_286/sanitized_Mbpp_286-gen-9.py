def max_sub_array_sum_repeated(arr, k, n):
  repeated_arr = arr * k
  max_sum = float('-inf')
  for i in range(n):
    window_sum = sum(repeated_arr[i:i+n])
    max_sum = max(max_sum, window_sum)
  return max_sum