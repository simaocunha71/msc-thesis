def max_sum(arr):
  arr.sort()
  max_sum = 0
  max_sum_bitonic_subsequence = 0
  for i in range(len(arr)):
    max_sum_bitonic_subsequence += arr[i]
    if max_sum_bitonic_subsequence < 0:
      max_sum_bitonic_subsequence = 0
    if max_sum_bitonic_subsequence > max_sum:
      max_sum = max_sum_bitonic_subsequence
  return max_sum