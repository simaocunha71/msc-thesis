def amicable_numbers_sum(n: int) -> int:
  sum = 0
  for i in range(1,n+1):
    if i == sum_of_divisors(i):
      sum += i
    if sum_of_divisors(i) == sum:
      sum += sum_of_divisors(i)
  return sum
def sum_of_divisors(n):
  return sum(i for i in range(1,int(n**0.5)+1) if n % i == 0)