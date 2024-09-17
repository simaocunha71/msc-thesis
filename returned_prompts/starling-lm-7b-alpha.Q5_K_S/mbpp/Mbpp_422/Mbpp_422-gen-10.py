
def find_Average_Of_Cube(n: int) -> float:
  cube_sum = 0
  for i in range(1, n+1):
    cube_sum += i**3
  return cube_sum / n


