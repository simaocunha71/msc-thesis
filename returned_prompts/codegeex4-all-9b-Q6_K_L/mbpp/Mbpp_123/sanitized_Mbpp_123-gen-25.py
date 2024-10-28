def amicable_numbers_sum(num):
  def sum_of_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])

  amicable_sum = 0
  for i in range(2, num):
    j = sum_of_divisors(i)
    if j != i and sum_of_divisors(j) == i:
      amicable_sum += i

  return amicable_sum