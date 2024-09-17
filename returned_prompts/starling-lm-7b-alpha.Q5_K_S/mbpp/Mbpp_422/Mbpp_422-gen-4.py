
def find_Average_Of_Cube(n):
  cubes_sum = 0
  for i in range(1, n+1):
    cubes_sum += i ** 3
  return cubes_sum / n


