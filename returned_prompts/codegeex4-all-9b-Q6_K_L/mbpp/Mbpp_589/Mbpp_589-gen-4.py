def perfect_squares(start: int,end: int) -> list:
  squares = []
  for i in range(start,end+1):
    if i**0.5 == int(i**0.5):
      squares.append(i)
  return squares

