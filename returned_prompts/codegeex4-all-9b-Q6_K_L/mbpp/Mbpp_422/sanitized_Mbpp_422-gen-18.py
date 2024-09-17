def find_Average_Of_Cube(n: int) -> float:
  sum_of_cubes = sum([i**3 for i in range(1, n+1)])
  average = sum_of_cubes / n
  return average