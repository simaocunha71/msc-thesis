def find_Average_Of_Cube(n):
  sum_cube = 0
  for i in range(1,n+1):
    sum_cube += i**3
  return sum_cube/n