def amicable_numbers_sum(n):
  sum = 0
  for i in range(1, n+1):
    if is_amicable(i):
      sum += i
  return sum

def is_amicable(n):
  sum_divisors = sum_divisors_of(n)
  return sum_divisors != n and sum_divisors_of(sum_divisors) == n

def sum_divisors_of(n):
  sum = 1
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      sum += i
      if i != n // i:
        sum += n // i
  return sum

