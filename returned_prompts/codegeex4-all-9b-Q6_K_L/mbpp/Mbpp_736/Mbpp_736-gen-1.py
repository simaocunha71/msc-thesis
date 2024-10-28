def left_insertion(nums: list, value: int) -> int:
  for i in range(len(nums)):
    if nums[i] >= value:
      return i
  return len(nums)


