def right_insertion(arr, num):
  l = 0
  r = len(arr) - 1
  while l <= r:
    mid = (l + r) // 2
    if arr[mid] == num:
      return mid
    if arr[mid] < num:
      l = mid + 1
    else:
      r = mid - 1
  return l