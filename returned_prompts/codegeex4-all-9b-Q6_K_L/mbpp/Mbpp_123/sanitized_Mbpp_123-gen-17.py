def amicable_numbers_sum(n):
  def sum_divisors(num):
    divisors = [1]
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        divisors.append(i)
        if i != num // i:
          divisors.append(num // i)
    return sum(divisors)

  amicable_numbers = []
  for i in range(2, n + 1):
    sum_i = sum_divisors(i)
    if sum_i != i and sum_divisors(sum_i) == i:
      amicable_numbers.append(i)

  return sum(amicable_numbers)