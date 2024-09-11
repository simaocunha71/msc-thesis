def index_multiplication(t1, t2):
  return tuple(tuple(a * b for a, b in zip(*t)) for t in zip(t1, t2))