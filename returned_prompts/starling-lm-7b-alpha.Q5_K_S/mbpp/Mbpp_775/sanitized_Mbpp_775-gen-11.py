def odd_position(nums: list) -> bool:
  for i in range(0, len(nums), 2):
    if nums[i]%2 != 1:
      return False
  return True