def max_Abs_Diff(arr):
  return max(abs(a - b) for a, b in zip(arr, arr[1:]))