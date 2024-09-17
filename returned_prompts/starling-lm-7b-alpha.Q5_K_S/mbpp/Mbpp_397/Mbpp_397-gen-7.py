
def median_numbers(a: int, b: int, c: int) -> float:
  if a < b:
    if b < c:
      return b
    elif a < c:
      return c
    else:
      return a
  elif a > b:
    if b > c:
      return b
    elif a > c:
      return c
    else:
      return a
  else:
    return c


