
def find_solution(a: int, b: int, n: int) -> tuple:
  x = (n * b + 1) // (a + b)
  if a * x - n == 0:
    return (x, 1)
  else:
    return None


