def max_sum_increasing_subseq(arr, n, k, i):
  max_sum = 0
  for j in range(i+1, k+1):
    max_sum = max(max_sum, arr[j] + max_sum_increasing_subseq(arr, n, k, j-1))
  return max_sum