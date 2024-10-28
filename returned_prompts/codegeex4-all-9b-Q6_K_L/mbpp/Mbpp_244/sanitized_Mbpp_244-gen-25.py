def next_Perfect_Square(n: int) -> int:
  if n < 0:
    return -1
  if math.sqrt(n) == int(math.sqrt(n)):
    return n + 1
  return int(math.sqrt(n) + 1) ** 2