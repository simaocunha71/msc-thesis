
def find_Average_Of_Cube(n: int) -> float:
  sum = 0
  for i in range(1, n+1):
    sum += (i**3)
  average = sum/n
  return average


