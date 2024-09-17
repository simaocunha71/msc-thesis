def max_sum_increasing_subseq(arr: list, i: int, j: int, k: int) -> int:
  if i > j or k < i or k > len(arr):
    return 0
  if i == j:
    return arr[i]
  if k == i:
    return max(arr[i], arr[i] + max_sum_increasing_subseq(arr, i+1, j, k))
  return max(arr[i] + max_sum_increasing_subseq(arr, i+1, j, k), max_sum_increasing_subseq(arr, i+1, j, k-1))