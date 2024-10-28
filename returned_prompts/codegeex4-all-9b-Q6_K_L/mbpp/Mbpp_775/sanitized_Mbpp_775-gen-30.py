def odd_position(nums: list) -> bool:
  return all(len([num for num in nums[i] if num % 2 == 1]) % 2 == 1 for i in range(1, len(nums), 2))