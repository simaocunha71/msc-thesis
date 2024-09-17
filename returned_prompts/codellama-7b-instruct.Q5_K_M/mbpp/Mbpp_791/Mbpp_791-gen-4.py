
def remove_nested(tup: tuple) -> tuple:
  return tuple(x for x in tup if not isinstance(x, tuple))


