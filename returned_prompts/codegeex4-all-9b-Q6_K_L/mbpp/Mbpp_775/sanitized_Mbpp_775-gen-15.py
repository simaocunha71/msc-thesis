def odd_position(nums: list) -> bool:
  odd_indices = nums[1::2]
  for num in odd_indices:
    if num % 2 == 0:
      return False
  return True