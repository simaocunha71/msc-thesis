def sum_even_and_even_index(nums: list) -> int:
  sum = 0
  for i in range(0, len(nums), 2):
    if nums[i] % 2 == 0:
      sum += nums[i]
  return sum


