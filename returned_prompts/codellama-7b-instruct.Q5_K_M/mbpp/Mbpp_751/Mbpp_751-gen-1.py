
def check_min_heap(arr):
  if len(arr) == 0 or len(arr) == 1:
    return True
  if arr[0] > arr[1]:
    return False
  i = 1
  while i < len(arr) // 2:
    left = 2 * i
    right = 2 * i + 1
    if left < len(arr) and arr[i] > arr[left]:
      return False
    if right < len(arr) and arr[i] > arr[right]:
      return False
    i += 1
  return True


