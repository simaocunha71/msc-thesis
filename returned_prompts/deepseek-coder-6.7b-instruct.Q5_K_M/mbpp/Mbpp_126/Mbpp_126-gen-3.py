
def sum_common_divisors(n1, n2):
  def divisors(n):
    return set(i for i in range(1, n+1) if n % i == 0)
  return sum(divisors(n1) & divisors(n2))


