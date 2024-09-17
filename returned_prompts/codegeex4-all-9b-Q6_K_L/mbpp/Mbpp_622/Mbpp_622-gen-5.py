def get_median(arr1: list, arr2: list, len_: int) -> float:
  arr = arr1 + arr2
  arr.sort()
  median = (arr[len_ // 2] + arr[-len_ // 2 - 1]) / 2
  return median