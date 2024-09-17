def left_insertion(nums, value):
  left = 0
  right = len(nums)
  while left < right:
    mid = (left + right) // 2
    if nums[mid] < value:
      left = mid + 1
    else:
      right = mid
  return left