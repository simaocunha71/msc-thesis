def max_sum_increasing_subseq(arr, n, k, i):
  if i >= n or k < 0:
    return 0
  if k == i:
    return arr[i]
  # Find the maximum sum of increasing subsequence from prefix until ith index
  # and including kth element
  return max(arr[i] + max_sum_increasing_subseq(arr, n, k - 1, i - 1),
             max_sum_increasing_subseq(arr, n, k, i - 1))