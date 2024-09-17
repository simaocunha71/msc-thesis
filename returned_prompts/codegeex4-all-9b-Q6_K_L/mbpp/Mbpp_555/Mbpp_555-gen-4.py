def difference(n):
  sum_natural_numbers = sum(range(1, n+1))
  sum_cubes_natural_numbers = sum([i**3 for i in range(1, n+1)])
  return sum_cubes_natural_numbers - sum_natural_numbers

