
def sequence(n: int) -> int:
  if n == 1:
    return 1
  else:
    return sequence(n - 1) + sequence(n - 2) + sequence(n - 3)


