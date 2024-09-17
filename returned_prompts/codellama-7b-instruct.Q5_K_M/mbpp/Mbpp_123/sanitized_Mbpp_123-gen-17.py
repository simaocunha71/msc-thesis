def amicable_numbers_sum(n: int) -> int:
  sum_of_amicable_numbers = 0
  for i in range(1,n+1):
    sum_of_divisors_of_i = sum(int(j) for j in str(i) if int(j) != 0 and int(j) != i)
    sum_of_divisors_of_sum_of_divisors_of_i = sum(int(j) for j in str(sum_of_divisors_of_i) if int(j) != 0 and int(j) != sum_of_divisors_of_i)
    if sum_of_divisors_of_i == i and sum_of_divisors_of_sum_of_divisors_of_i == sum_of_divisors_of_i and sum_of_divisors_of_i != sum_of_divisors_of_sum_of_divisors_of_i:
      sum_of_amicable_numbers += i
  return sum_of_amicable_numbers