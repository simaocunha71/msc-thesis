def is_Monotonic(arr):
  n = len(arr)
  if n == 1:
    return True
  if arr[0] > arr[-1]:
    return False
  for i in range(1,n):
    if arr[i] < arr[i-1]:
      return False
  return True