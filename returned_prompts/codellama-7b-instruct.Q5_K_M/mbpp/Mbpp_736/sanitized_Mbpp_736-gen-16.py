def left_insertion(my_list, val):
  left = 0
  right = len(my_list) - 1
  while left <= right:
    mid = (left + right) // 2
    if my_list[mid] >= val:
      right = mid - 1
    else:
      left = mid + 1
  return left