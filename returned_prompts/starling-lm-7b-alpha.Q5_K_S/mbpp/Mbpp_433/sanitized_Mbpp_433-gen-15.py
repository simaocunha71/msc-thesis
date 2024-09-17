def check_greater(nums:list, num:int) -> bool:
  for i in range(len(nums)):
    if num > nums[i]:
      return True
  return False