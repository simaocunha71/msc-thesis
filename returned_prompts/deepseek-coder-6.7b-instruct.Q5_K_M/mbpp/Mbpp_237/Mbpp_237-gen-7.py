
def check_occurences(lst):
  d = {}
  for tup in lst:
    d[tup] = d.get(tup, 0) + 1
  return d


