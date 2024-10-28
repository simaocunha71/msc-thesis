def perfect_squares(n:int, m:int) -> list:
  squares = []
  for i in range(n, m+1):
    if int(i ** 0.5) ** 2 == i:
      squares.append(i)
  return squares