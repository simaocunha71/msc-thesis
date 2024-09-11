def max_sub_array_sum_repeated(arr, n, k):
  modified_arr = arr * k
  max_sum = float('-inf')
  window_sum = 0
  for i in range(len(modified_arr)):
    window_sum += modified_arr[i]
    if i >= n:
      window_sum -= modified_arr[i-n]
    max_sum = max(max_sum, window_sum)
  return max_sum