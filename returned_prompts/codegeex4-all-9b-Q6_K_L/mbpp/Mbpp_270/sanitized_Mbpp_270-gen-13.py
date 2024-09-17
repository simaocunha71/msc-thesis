def sum_even_and_even_index(nums: list) -> int:
  return sum(nums[i] for i in range(len(nums)) if i % 2 == 0 and nums[i] % 2 == 0)