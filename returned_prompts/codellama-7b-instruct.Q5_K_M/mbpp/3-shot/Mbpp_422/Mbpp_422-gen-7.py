
def find_Average_Of_Cube(n):
  sum_of_cubes = 0
  for i in range(n):
    sum_of_cubes += (i**3)
  average_of_cubes = sum_of_cubes/n
  return average_of_cubes


