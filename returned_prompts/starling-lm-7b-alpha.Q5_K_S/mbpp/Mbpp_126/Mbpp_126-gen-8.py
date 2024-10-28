
def sum_divisors(n1: int, n2: int) -> int:
  divisors_n1 = set()
  for i in range(1, int(math.sqrt(n1)) + 1):
    if n1 % i == 0:
      divisors_n1.add(i)
      divisors_n1.add(n1//i)
  divisors_n2 = set()
  for j in range(1, int(math.sqrt(n2)) + 1):
    if n2 % j == 0:
      divisors_n2.add(j)
      divisors_n2.add(n2//j)
  return len(divisors_n1 & divisors_n2)


