def sum_divisors(n):
  sum = 1
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      sum += i
      if i * i != n:
        sum += n // i
  return sum
def amicable_numbers_sum(limit):
  sum = 0
  for i in range(1, limit+1):
    div_sum = sum_divisors(i)
    if div_sum > i and sum_divisors(div_sum) == i:
      sum += i
  return sum