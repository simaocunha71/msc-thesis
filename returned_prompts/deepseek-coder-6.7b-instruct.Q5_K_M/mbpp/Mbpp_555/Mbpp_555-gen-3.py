
def difference(n):
  sum_of_cubes = sum([i**3 for i in range(1, n+1)])
  sum_of_numbers = sum([i for i in range(1, n+1)])
  return abs(sum_of_cubes - sum_of_numbers)

