def tuple_to_dict(tup):
  d = {}
  for i in range(0, len(tup)-1, 2):
    d[tup[i]] = tup[i + 1]
  return d