def issort_list(nums: list) -> bool:
  if len(nums) == 0 or len(nums) == 1:
    return True
  for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
      return False
  return True