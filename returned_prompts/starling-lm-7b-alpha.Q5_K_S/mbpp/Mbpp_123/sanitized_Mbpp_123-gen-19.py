def amicable_numbers_sum(n: int) -> int:
  amicable_nums = []
  for i in range(1,n+1):
    if i == sum(divisors(i))-i:
      amicable_nums.append(i)
  return sum(amicable_nums)
def divisors(n: int) -> list:
  divisors = []
  for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
      if n // i == i:
        divisors.append(i)
      else:
        divisors.append(i)
        divisors.append(n//i)
  return divisors