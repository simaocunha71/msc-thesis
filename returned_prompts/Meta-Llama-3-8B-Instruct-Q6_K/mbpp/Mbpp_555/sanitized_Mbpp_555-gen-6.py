def difference(n):
  sum_of_natural_numbers = n * (n + 1) // 2
  sum_of_cubes = sum(i ** 3 for i in range(1, n + 1))
  return sum_of_cubes - sum_of_natural_numbers