def right_insertion(nums: list, val: int) -> int:
  for i in range(len(nums)):
    if nums[i]>val:
      return i
  return len(nums)