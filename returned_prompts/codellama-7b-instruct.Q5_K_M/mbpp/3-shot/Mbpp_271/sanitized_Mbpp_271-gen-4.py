def even_Power_Sum(n):
  sum_even_power = 0
  for i in range(0, n):
    sum_even_power += (i * 2) ** 5
  return sum_even_power