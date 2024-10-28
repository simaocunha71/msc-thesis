
def perfect_squares(low: int, high: int) -> list:
  squares = []
  for i in range(low, high + 1):
    if i**2 <= high:
      squares.append(i**2)
  return squares


