def difference(n: int) -> int:
  cube_sum = sum([i**3 for i in range(1, n+1)])
  natural_sum = sum([i for i in range(1, n+1)])
  return cube_sum - natural_sum