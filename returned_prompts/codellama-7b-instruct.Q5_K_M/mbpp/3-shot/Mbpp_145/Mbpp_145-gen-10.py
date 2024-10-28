
def max_Abs_Diff(arr: list) -> int:
  return max(map(lambda x,y: abs(x-y), arr, arr[1:]))


