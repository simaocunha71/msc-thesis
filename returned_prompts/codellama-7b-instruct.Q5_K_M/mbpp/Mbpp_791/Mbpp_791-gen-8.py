
def remove_nested(tup):
  return tuple(map(lambda x: x if isinstance(x, tuple) else x[0], tup))


