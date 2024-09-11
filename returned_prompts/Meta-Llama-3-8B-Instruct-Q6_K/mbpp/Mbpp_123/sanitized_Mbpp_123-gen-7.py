def amicable_numbers_sum(n):
  def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
      if num % i == 0:
        total += i
    return total

  sum_total = 0
  for i in range(1, n+1):
    if sum_of_divisors(i) > i and sum_of_divisors(sum_of_divisors(i)) == i:
      sum_total += i
  return sum_total