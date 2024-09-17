def last(nums:list, target:int) -> int:
  left = 0
  right = len(nums)-1
  while left <= right:
    mid = left + (right-left)//2
    if nums[mid] == target:
      left = mid + 1
    elif target < nums[mid]:
      right = mid - 1
    else:
      left = mid + 1
  if left == len(nums):
    return -1
  else:
    return left