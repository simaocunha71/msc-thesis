
def sum_common_divisors(n1: int, n2: int) -> int:
  common_divisors = set(divisors(n1)) & set(divisors(n2))
  return sum(common_divisors)

def divisors(n: int) -> set:
  divisors = set()
  for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
      divisors.add(i)
      divisors.add(n//i)
  return divisors


