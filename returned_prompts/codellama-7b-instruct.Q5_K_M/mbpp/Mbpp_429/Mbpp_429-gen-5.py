
def and_tuples(tup1, tup2) -> tuple:
  return tuple(x & y for x, y in zip(tup1, tup2))

