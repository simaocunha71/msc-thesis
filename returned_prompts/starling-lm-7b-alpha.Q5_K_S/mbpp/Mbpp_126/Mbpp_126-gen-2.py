
def sum_common_divisors(n1: int, n2: int) -> int:
  lcm = lcm(n1,n2)
  i = 1
  sum = 0
  while i <= lcm:
    if n1 % i == 0 and n2 % i == 0:
      sum += i
    i += 1
  return sum

def lcm(n1: int, n2: int) -> int:
  return n1 * n2 // gcd(n1, n2)

def gcd(n1: int, n2: int) -> int:
  while n2 != 0:
    n1, n2 = n2, n1 % n2
  return n1


