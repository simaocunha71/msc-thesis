def difference(n: int) -> int:
  sum_of_cubes = sum([i**3 for i in range(n+1)])
  sum_of_nums = sum(range(n+1))
  return sum_of_cubes - sum_of_nums