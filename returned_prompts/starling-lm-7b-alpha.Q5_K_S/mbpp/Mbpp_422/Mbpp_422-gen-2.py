
def find_Average_Of_Cube(n: int) -> float:
  total_cube = 0
  for i in range(1,n+1):
    total_cube += i**3
  return total_cube/n


