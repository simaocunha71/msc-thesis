def and_tuples(tup1: tuple,tup2: tuple) -> tuple:
  return tuple(map(lambda x,y: x&y, tup1, tup2))