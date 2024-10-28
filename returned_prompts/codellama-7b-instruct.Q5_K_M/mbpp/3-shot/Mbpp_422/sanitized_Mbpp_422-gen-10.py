def find_Average_Of_Cube(n):
  sum_of_cube = 0
  for i in range(1, n+1):
    sum_of_cube += i**3
  return sum_of_cube/(n*(n+1)*(2*n+1))