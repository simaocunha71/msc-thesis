def sum_even_and_even_index(nums):
  return sum(nums[i] for i in range(0, len(nums), 2) if nums[i] % 2 == 0)