
def index_multiplication(tup1: tuple, tup2: tuple) -> tuple:
  return tuple(map(lambda x,y: (x*y[0], y[1]), tup1, tup2))


