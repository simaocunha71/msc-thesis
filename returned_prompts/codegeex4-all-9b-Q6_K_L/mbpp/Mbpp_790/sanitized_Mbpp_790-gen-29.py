def even_position(nums: list) -> bool:
  for index in range(0, len(nums), 2):
    if nums[index] % 2 != 0:
      return False
  return True