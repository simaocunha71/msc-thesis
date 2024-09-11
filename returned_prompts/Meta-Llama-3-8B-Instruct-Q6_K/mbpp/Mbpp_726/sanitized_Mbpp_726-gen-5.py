def multiply_elements(tup):
  return tuple(t * t for t in tup[:-1])  # using generator expression