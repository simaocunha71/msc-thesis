def d(n):
  return sum(i for i in range(1, n) if n % i == 0)
def amicable_numbers_sum(n):
  return sum(i for i in range(1, n) if d(d(i)) == i and i != d(i))