def sum_of_digits(nums:list) -> int:
  total_sum = 0
  for num in nums:
    total_sum += sum(map(int,str(num)))
  return total_sum