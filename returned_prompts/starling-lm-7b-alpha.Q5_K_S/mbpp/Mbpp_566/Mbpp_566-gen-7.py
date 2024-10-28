
def sum_digits(num: int) -> int:
  sum_num = 0
  while num > 0:
    sum_num += num % 10
    num //= 10
  return sum_num


