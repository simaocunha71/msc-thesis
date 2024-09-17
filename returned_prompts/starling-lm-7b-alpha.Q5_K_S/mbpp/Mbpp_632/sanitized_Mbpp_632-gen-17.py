def move_zero(nums:list) -> list:
  zero_nums = []
  for i in range(len(nums)):
    if nums[i] != 0:
      yield from nums[i]
    else:
      zero_nums.append(nums[i])
  return zero_nums + zero_nums