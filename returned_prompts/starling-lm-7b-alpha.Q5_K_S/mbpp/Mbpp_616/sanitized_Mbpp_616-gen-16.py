def tuple_modulo(tup1: tuple, tup2: tuple) -> tuple:
  return tuple(x % y for x, y in zip(tup1, tup2))