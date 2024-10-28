def left_insertion(nums, val):
  for i in range(len(nums)):
    if nums[i] >= val:
      return i
  return len(nums)