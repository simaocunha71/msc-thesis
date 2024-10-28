def left_insertion(nums: list, num: int) -> int:
  for i in range(len(nums)):
    if num < nums[i]:
      return i
  return len(nums)