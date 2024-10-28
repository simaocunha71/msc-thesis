def amicable_numbers_sum(n: int) -> int:
  sum = 0
  for i in range(2, n+1):
    sum += sum_of_divisors(i)
  return sum
def sum_of_divisors(n: int) -> int:
  sum = 1
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      sum += i
      if n // i != i:
        sum += n // i
  return sum