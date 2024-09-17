def last(arr: list, key: int) -> int:
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = low + (high - low) // 2
    if arr[mid] == key:
      if mid == len(arr) - 1:
        return mid
      else:
        low = mid + 1
    elif arr[mid] < key:
      low = mid + 1
    else:
      high = mid - 1
  return -1