def sum_of_digits(nums: list) -> int:
  total = 0
  for num in nums:
    total += sum(map(int,str(num)))
  return total