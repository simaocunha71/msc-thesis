def last(nums: list, target: int) -> int:
  l = 0
  r = len(nums) - 1
  while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
      l = mid + 1
    elif nums[mid] < target:
      l = mid + 1
    else:
      r = mid - 1
  return l - 1