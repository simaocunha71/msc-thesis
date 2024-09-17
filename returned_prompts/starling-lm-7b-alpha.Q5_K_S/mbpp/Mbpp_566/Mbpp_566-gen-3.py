
def sum_digits(num: int) -> int:
  sum = 0
  while(num):
    sum += num % 10
    num //= 10
  return sum


