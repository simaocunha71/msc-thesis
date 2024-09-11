def odd_num_sum(n):
  return sum(i ** 4 for i in range(1, n * 2, 2))  # Generate all odd numbers up to 2n-1, square them, and sum them