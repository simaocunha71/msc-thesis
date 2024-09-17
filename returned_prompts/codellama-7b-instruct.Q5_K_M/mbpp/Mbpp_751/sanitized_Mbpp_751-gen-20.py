def check_min_heap(arr):
  if len(arr) == 1:
    return True
  if len(arr) == 2:
    return True
  if arr[0] > arr[1]:
    return False
  if arr[1] > arr[2]:
    return False
  return check_min_heap(arr[1:]) and check_min_heap(arr[2:])