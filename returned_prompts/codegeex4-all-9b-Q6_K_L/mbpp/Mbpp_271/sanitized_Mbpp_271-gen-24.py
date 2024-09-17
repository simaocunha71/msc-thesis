def even_Power_Sum(n):
  sum_even_power = 0
  for i in range(2, 2*n+1, 2):
    sum_even_power += i**5
  return sum_even_power