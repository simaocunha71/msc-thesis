def maximize_elements(tup1, tup2):
  return tuple((max(a, b), max(c, d)) for a, b, c, d in zip(tup1, tup2))