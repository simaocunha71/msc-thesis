
def find_solution(a: int, b: int, n: int) -> tuple:
  if a == 0:
    return None
  x = n // b
  y = n % b
  return (x, y)


