def index_multiplication(tuple1, tuple2):
  return tuple(map(lambda x, y: tuple(map(lambda u, v: u*v, x, y)), tuple1, tuple2))