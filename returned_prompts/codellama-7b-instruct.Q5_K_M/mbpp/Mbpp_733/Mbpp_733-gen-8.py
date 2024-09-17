
def find_first_occurrence(arr: list, num: int) -> int:
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == num:
      right = mid - 1
    elif arr[mid] > num:
      right = mid - 1
    else:
      left = mid + 1
  if left < len(arr) and arr[left] == num:
    return left
  return -1


