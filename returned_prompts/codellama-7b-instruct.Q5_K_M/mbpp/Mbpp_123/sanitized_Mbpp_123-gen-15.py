def amicable_numbers_sum(n):
  sums = []
  for i in range(1, n+1):
    sum_of_divisors_1 = sum(list(set(range(1, i+1)) & set(range(1, i))))
    sum_of_divisors_2 = sum(list(set(range(1, sum_of_divisors_1+1)) & set(range(1, sum_of_divisors_1))))
    if sum_of_divisors_1 == i and sum_of_divisors_2 == sum_of_divisors_1:
      sums.append(sum_of_divisors_1)
  return sum(sums)