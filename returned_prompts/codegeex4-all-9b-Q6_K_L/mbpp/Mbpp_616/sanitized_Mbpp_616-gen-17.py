def tuple_modulo(tup1, tup2):
  result = tuple(x % y for x, y in zip(tup1, tup2))
  return result