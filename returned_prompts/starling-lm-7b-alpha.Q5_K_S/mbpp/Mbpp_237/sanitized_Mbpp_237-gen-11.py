def check_occurences(list_tuples):
  d = {}
  for tup in list_tuples:
    if tup not in d:
      d[tup] = 0
    d[tup] += 1
  return d