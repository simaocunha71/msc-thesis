
def check_min_heap(arr: list) -> bool:
  n = len(arr)
  if n == 1:
    return True
  for i in range(n//2-1, -1, -1):
    if arr[i] > arr[i * 2 + 1]:
      return False
    if i * 2 + 2 < n and arr[i] > arr[i * 2 + 2]:
      return False
  return True


