def find_solution(a: int, b: int, n: int) -> tuple:
  if a == 0:
    return None
  x, y = 0, n // a
  if a * x + b * y == n:
    return x, y
  for x, y in [(x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1), (x - 1, y - 1)]:
    if a * x + b * y == n:
      return x, y
  return None