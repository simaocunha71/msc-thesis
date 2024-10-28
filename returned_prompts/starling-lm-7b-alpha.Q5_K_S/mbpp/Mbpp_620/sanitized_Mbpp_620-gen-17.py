def largest_subset(nums:list) -> int:
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return 1
  elif len(nums) == 2:
    if nums[0] % nums[1] == 0:
      return 2
    else:
      return 1
  else:
    if nums[-1] % nums[-2] == 0:
      return 1 + largest_subset(nums[:-2])
    else:
      return 1 + largest_subset(nums[:-1])