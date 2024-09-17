
def sum_common_divisors(x, y):
  def divisors(n):
    i = 1
    divs = []
    while i <= n:
      if n % i == 0:
        divs.append(i)
      i += 1
    return divs
  return sum(set(divisors(x)) & set(divisors(y)))


