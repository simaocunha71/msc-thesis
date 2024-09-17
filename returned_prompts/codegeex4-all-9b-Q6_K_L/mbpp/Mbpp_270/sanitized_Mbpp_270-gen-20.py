def sum_even_and_even_index(nums: list) -> int:
  total = 0
  for i in range(len(nums)):
    if i % 2 == 0 and nums[i] % 2 == 0:
      total += nums[i]
  return total