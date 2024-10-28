
def sum_of_digits(nums: list) -> int:
  sum_of_digits = 0
  for n in nums:
    while n > 0:
      sum_of_digits += n % 10
      n = n//10
  return sum_of_digits


