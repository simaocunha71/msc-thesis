def left_insertion(lst, val):
  low = 0
  high = len(lst)
  while low < high:
    mid = (low + high) // 2
    if lst[mid] < val:
      low = mid + 1
    else:
      high = mid
  return low