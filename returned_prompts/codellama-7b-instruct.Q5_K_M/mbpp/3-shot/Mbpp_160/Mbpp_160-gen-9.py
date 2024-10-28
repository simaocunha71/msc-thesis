
def find_solution(a: int, b: int, n: int) -> tuple:
  x = n // b
  y = n % b
  if a * y == n:
    return (x, y)
  else:
    return None


