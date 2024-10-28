
def sum_of_digits(nums:list) -> int:
  sum_digits = 0
  for num in nums:
    while num > 0:
      sum_digits += num % 10
      num = num // 10
  return sum_digits


