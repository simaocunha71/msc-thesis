def amicable_numbers_sum(n: int) -> int:
  sum = 0
  for i in range(1, n+1):
    if i != sum(get_amicable_numbers(i)):
      sum += i
  return sum
def get_amicable_numbers(n: int) -> list:
  sum = 0
  for i in range(1, n):
    if n % i == 0:
      sum += i
  return [n, sum]