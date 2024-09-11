def amicable_numbers_sum(n):
  def sum_of_divisors(num):
    sum_divisors = 0
    for i in range(1, num):
      if num % i == 0:
        sum_divisors += i
    return sum_divisors

  total_sum = 0
  for i in range(1, n+1):
    if sum_of_divisors(i) == i:
      continue
    sum_divisors = sum_of_divisors(i)
    if sum_of_divisors == i:
      continue
    if sum_of_divisors(i) == i:
      total_sum += i + sum_of_divisors(i)
  return total_sum