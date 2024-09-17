def find_dissimilar(tup1,tup2):
  result = list(set(tup1) ^ set(tup2))
  return tuple(result)