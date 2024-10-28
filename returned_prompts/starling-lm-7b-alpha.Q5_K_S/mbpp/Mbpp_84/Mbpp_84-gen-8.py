
def sequence(n: int) -> int:
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return sequence(n-1) + sequence(n-2)


