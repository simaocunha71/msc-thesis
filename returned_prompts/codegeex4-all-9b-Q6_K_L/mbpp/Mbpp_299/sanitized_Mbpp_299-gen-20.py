def max_aggregate(tup_list: list) -> tuple:
  aggregate = {}
  for tup in tup_list:
    if tup[0] in aggregate:
      aggregate[tup[0]] += tup[1]
    else:
      aggregate[tup[0]] = tup[1]
  max_aggregate = max(aggregate, key=aggregate.get)
  return (max_aggregate, aggregate[max_aggregate])