def check_min_heap(nums: list) -> bool:
  for i in range(1, len(nums)):
    if nums[i] < nums[i//2]:
      return False
  return True