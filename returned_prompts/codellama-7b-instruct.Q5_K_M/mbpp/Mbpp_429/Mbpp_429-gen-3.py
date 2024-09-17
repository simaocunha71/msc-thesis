
def and_tuples(tup1, tup2):
  return tuple(tup1[i] & tup2[i] for i in range(len(tup1)))


