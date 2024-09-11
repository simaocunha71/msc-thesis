def amicable_numbers_sum(n):
  def is_amicable(a):
    b = sum(i for i in range(1, a) if a % i == 0)
    if b == a:
      return False
    return sum(i for i in range(1, b) if b % i == 0) == a

  return sum(i for i in range(1, n+1) if is_amicable(i))  # This is not efficient, you might want to optimize this