
def max_sum_increasing_subseq(arr: list, i: int, k: int, x: int) -> int:
  if i == k:
    return arr[i]
  elif i > k:
    return max(arr[i], max_sum_increasing_subseq(arr, i-1, k, x) + arr[i])
  else:
    return max_sum_increasing_subseq(arr, i+1, k, x)


