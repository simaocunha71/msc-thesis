
def sum_of_common_divisors(a, b):
  def divisors(n):
    i, divs = 1, []
    while i <= n:
        if n % i == 0: divs.append(i)
        i += 1
    return divs
  return sum(set(divisors(a)) & set(divisors(b)))


