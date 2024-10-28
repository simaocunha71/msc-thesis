
def sum_even_and_even_index(nums:list) -> int:
  sum = 0
  for i in range(len(nums)):
    if i % 2 == 0 and nums[i] % 2 == 0:
      sum += nums[i]
  return sum


