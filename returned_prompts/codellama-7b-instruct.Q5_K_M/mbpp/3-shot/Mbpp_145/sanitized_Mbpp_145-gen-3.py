def max_Abs_Diff(arr: list) -> int:
  return max(map(abs, zip(arr, arr[1:])))