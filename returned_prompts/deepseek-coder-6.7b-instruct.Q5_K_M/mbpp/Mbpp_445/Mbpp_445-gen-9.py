
def index_multiplication(tup1, tup2):
  return tuple(tuple(a*b for a, b in zip(*x)) for x in zip(tup1, tup2))


