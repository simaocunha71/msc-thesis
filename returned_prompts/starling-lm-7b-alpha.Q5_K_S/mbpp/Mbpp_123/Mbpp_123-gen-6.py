
def amicable_numbers_sum(n):
  amicable_numbers = []
  for i in range(1, n + 1):
    if i == sum(divisors(i)) - i:
      amicable_numbers.append(i)
  return sum(amicable_numbers)

def divisors(n):
  dvs = []
  for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
      dvs.append(i)
      if i != n // i:
        dvs.append(n // i)
  return dvs


