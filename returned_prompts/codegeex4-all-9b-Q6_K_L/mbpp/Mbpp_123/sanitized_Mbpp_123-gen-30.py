def amicable_numbers_sum(num):
  def is_amicable(n):
    sum1 = sum([i for i in range(1, n) if n % i == 0])
    sum2 = sum([i for i in range(1, sum1) if sum1 % i == 0])
    return sum2 == n and sum2 != sum1
  return sum([i for i in range(1, num + 1) if is_amicable(i)])