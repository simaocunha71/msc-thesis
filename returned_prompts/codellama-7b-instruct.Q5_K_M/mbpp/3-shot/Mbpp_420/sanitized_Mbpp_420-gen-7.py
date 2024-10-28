def cube_Sum(n):
  sum_of_cubes = 0
  for i in range(0, n, 1):
    sum_of_cubes += i * i * i
  return sum_of_cubes