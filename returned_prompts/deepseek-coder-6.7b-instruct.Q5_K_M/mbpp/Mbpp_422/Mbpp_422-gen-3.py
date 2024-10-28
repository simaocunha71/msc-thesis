
def find_Average_Of_Cube(n):
  total_cube_sum = sum(i**3 for i in range(1, n+1))
  average = total_cube_sum / n
  return average


