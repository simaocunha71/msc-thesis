def is_perfect_square(n: int) -> bool:
  if n < 0:
    return False
  return math.isqrt(n) ** 2 == n