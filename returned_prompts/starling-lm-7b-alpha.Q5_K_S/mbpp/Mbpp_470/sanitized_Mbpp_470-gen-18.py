def add_pairwise(tup: tuple) -> tuple:
  return tuple(a+b for a, b in zip(tup[:-1], tup[1:]))