def max_aggregate(list_tuples):
  name = list_tuples[0][0]
  aggregate = list_tuples[0][1]
  for tup in list_tuples:
    if tup[0] == name:
      aggregate += tup[1]
    else:
      name = tup[0]
      aggregate = tup[1]
  return (name, aggregate)

