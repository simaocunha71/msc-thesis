def odd_position(nums: list) -> bool:
  return all(len(str(nums[i])) % 2 == 1 for i in range(len(nums)) if i % 2 == 1)

