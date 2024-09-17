def perfect_squares(start: int, end: int) -> list:
  squares = []
  for i in range(start, end+1):
    root = int(math.sqrt(i))
    if root*root == i:
      squares.append(i)
  return squares