def amicable_numbers_sum(n: int) -> int:
  amicable_nums = set()
  for i in range(1,n+1):
    if i <= 1:
      continue
    x = sum_divisors(i)
    if x != i:
      if x <= n:
        amicable_nums.add(x)
  return sum(amicable_nums)
def sum_divisors(n: int) -> int:
  divisors = set()
  for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:
      divisors.add(i)
      if n//i != i:
        divisors.add(n//i)
  return sum(divisors)