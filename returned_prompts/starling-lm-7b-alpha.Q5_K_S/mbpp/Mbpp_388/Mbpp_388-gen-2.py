
def highest_Power_of_2(n: int) -> int:
  while n % 2 == 0:
    n = n // 2
  return n


