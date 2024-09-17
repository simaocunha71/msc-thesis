def find_tuples(tups, k):
  return list(filter(lambda x: all(y % k == 0 for y in x), tups))