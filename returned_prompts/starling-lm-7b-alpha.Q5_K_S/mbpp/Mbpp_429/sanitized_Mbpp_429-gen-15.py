def and_tuples(t1:tuple, t2:tuple) -> tuple:
  return tuple(map(lambda x,y: x&y, t1, t2))