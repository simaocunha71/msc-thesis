def find_Average_Of_Cube(n):
  sum_cubes = sum([i**3 for i in range(1, n+1)])
  return sum_cubes/n