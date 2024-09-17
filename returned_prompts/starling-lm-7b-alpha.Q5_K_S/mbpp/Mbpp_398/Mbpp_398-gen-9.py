
def sum_of_digits(nums: list) -> int:
  sum_digits = 0
  for n in nums:
    sum_digits += sum(map(int, str(n)))
  return sum_digits


