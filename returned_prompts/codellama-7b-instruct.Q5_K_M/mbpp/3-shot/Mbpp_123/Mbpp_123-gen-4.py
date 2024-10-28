
def amicable_numbers_sum(n: int) -> int:
  sum = 0
  for i in range(1, n+1):
    d1 = sum(list(map(int, str(i))))
    d2 = sum(list(map(int, str(d1))))
    if d2 == i and d1 != i:
      sum += i
  return sum


