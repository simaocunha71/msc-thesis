def even_position(nums: list) -> bool:
  return all(nums[i] % 2 == 0 for i in range(0, len(nums), 2))

