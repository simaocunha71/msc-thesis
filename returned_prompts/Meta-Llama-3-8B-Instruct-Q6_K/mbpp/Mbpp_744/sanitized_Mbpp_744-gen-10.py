def check_none(tup):
  return any(isinstance(x, type(None)) for x in tup) if len(tup) > 0 else False