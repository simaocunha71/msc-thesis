def right_insertion(sorted_list, target):
  left = 0
  right = len(sorted_list) - 1
  while left <= right:
    mid = (left + right) // 2
    if sorted_list[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return left