
def find_solution(a: int, b: int, n: int) -> tuple:
  if a == 0:
    if b == 0:
      return None
    else:
      return (0, n // b)
  else:
    x = n % b
    y = n // b
    if x == 0:
      return (y, 0)
    else:
      sol = find_solution(b, a, x)
      if sol:
        return (sol[1], sol[0])
      else:
        return None


