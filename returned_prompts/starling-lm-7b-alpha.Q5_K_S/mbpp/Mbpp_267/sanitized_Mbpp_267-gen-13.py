def square_Sum(n: int) -> int:
  return sum([i**2 for i in range(1, 2*n+1, 2)])