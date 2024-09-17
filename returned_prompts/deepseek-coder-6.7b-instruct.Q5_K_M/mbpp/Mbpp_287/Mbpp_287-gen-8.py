
def square_Sum(n):
  sum = 0
  for i in range(2, 2*n+1, 2):
    sum += i**2
  return sum


