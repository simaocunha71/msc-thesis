def check_min_heap(arr: list) -> bool:
  for i in range(len(arr)):
    j = 2 * i + 1
    k = 2 * i + 2
    if j < len(arr) and arr[j] < arr[i]:
      return False
    if k < len(arr) and arr[k] < arr[i]:
      return False
  return True