
def perfect_squares(start: int,end: int) -> list:
  perfect_squares = []
  for i in range(start,end+1):
    root = i ** 0.5
    if root % 1 == 0:
      perfect_squares.append(i)
  return perfect_squares


