def perfect_squares(start: int, end: int) -> list:
  return [i ** 2 for i in range(int(math.sqrt(start)), int(math.sqrt(end)) + 1)]