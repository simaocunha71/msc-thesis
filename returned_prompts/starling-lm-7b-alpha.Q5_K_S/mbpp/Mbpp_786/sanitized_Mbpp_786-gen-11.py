def right_insertion(nums: list, target: int) -> int:
  left = 0
  right = len(nums)-1
  while left<right:
    mid = int((left+right)/2)
    if nums[mid] < target:
      left = mid+1
    else:
      right = mid-1
  if target < nums[left]:
    return left
  else:
    return right