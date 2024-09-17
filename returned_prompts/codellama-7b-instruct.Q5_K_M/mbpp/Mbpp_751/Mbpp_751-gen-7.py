
def check_min_heap(arr):
  n = len(arr)
  if n == 1:
    return True
  for i in range(n // 2):
    if arr[i] > arr[i * 2] or arr[i] > arr[i * 2 + 1]:
      return False
  return True


