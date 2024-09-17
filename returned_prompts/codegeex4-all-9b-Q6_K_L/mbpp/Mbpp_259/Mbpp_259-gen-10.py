def maximize_elements(tup1, tup2):
  return tuple(sorted(zip(tup1, tup2), key=lambda x: (x[0], x[1]), reverse=True))

