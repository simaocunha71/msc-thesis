
def difference(n):
  sum_cubes = sum([i**3 for i in range(1, n+1)])
  sum_nums = sum([i for i in range(1, n+1)])
  return sum_cubes - sum_nums


