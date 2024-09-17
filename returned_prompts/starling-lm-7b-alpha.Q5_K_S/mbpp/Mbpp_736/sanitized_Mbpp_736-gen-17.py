def left_insertion(nums: list, x: int) -> int:
  if x < nums[0]:
    return 0
  elif x > nums[-1]:
    return len(nums)
  else:
    for i in range(len(nums)):
      if x > nums[i]:
        if i == 0:
          return 0
        else:
          return i
      elif x < nums[i]:
        return i
    return len(nums)