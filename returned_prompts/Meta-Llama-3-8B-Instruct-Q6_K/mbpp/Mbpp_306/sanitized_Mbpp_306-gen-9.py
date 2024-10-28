def max_sum_increasing_subseq(arr, i, k, j):
  prefix_sum = sum(arr[:i])
  max_sum = prefix_sum
  for idx in range(i, j):
    if arr[idx] > arr[idx-1]:
      max_sum += arr[idx]
  return max_sum