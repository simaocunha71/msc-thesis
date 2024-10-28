def amicable_numbers_sum(n: int) -> int:
  sum = 0
  for i in range(1,n+1):
    sum_of_proper_divisors = sum(i for i in range(1, int(i**0.5)+1) if i % i == 0 and i // i == i)
    sum_of_proper_divisors2 = sum(i for i in range(1, int(i**0.5)+1) if i % i == 0 and i // i == i)
    if sum_of_proper_divisors == i and sum_of_proper_divisors2 < i:
      sum += i
  return sum