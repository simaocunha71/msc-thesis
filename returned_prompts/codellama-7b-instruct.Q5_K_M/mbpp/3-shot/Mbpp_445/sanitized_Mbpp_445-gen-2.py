def index_multiplication(tup1, tup2):
  assert len(tup1) == len(tup2)
  return tuple(x*y for x, y in zip(tup1, tup2))