
def remove_nested(tup):
  return tuple(filter(lambda x: not isinstance(x, tuple), tup))


