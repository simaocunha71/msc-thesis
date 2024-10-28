def last(arr, element):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == element:
      left = mid + 1
    else:
      right = mid - 1
  if left < len(arr) and arr[left] == element:
    return left
  return -1