def add_pairwise(tup: tuple) -> tuple:
  return tuple(tup[i] + tup[i+1] for i in range(len(tup)-1))