def square_Sum(n: int) -> int:
  total = 0
  for i in range(1, n*2, 2):
    total += i**2
  return total