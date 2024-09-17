def even_position(nums: list) -> bool:
  even_indices = [nums[i] for i in range(len(nums)) if i % 2 == 0]
  return all(num % 2 == 0 for num in even_indices)