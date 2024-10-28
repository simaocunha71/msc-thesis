def find_dissimilar(tup1,tup2):
  set1 = set(tup1)
  set2 = set(tup2)
  dissimilar = list(set1 ^ set2)
  return tuple(dissimilar)