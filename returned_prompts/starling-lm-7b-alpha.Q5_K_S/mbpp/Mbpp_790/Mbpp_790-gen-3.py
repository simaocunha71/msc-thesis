
def even_position(nums: list) -> bool:
  for i in range(0, len(nums), 2):
    if nums[i] % 2 != 0:
      return False
  return True


