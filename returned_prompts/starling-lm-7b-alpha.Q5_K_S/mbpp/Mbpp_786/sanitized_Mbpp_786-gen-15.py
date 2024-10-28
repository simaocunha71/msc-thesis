def right_insertion(sorted_list:list, target:int) -> int:
  left = 0
  right = len(sorted_list) - 1
  while left <= right:
    mid = (left + right) // 2
    if target < sorted_list[mid]:
      right = mid - 1
    elif target > sorted_list[mid]:
      left = mid + 1
    else:
      return mid
  return left