
def sum_even_and_even_index(nums: list) -> int:
  sum_even = 0
  for i,num in enumerate(nums):
    if i % 2 == 0 and num % 2 == 0:
      sum_even += num
  return sum_even


