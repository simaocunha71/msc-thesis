def difference(n: int) -> int:
  sum_natural = n * (n + 1) // 2
  sum_cubes = (n * (n + 1) // 2) ** 2
  return sum_cubes - sum_natural