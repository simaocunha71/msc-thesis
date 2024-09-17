def right_insertion(nums: list,num: int) -> int:
  for i in range(len(nums)):
    if nums[i] >= num:
      return i
  return len(nums)

