
def right_insertion(arr, x):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
      return mid + 1
    elif arr[mid] > x:
      high = mid - 1
    else:
      low = mid + 1
  return low


