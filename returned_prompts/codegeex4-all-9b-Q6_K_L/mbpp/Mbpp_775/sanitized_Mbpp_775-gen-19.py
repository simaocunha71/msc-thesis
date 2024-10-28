def odd_position(nums: list) -> bool:
  for index in range(1, len(nums), 2):
    if nums[index] % 2 == 0:
      return False
  return True