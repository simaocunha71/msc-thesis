def remove_nested(tup: tuple) -> tuple:
  return tuple(filter(lambda x: not isinstance(x, tuple), tup))