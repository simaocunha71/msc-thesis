
def amicable_numbers_sum(n: int) -> int:
  sum_ = 0
  for i in range(1, n+1):
    if is_amicable(i):
      sum_ += i
  return sum_

def is_amicable(n: int) -> bool:
  s = 0
  for i in range(1, n):
    if n % i == 0:
      s += i
  if s != 1:
    return is_amicable(s)
  return False


