def left_insertion(nums: list, target: int) -> int:
  left = 0
  right = len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return left