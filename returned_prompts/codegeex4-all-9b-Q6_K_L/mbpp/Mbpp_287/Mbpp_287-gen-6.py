def square_Sum(n: int) -> int:
  if n<0:
    return "Invalid input"
  else:
    return sum(i**2 for i in range(2*n+1, 1, -2))

