def max_aggregate(tuples: list) -> tuple:
  aggregate_dict = {}
  for name, score in tuples:
    if name in aggregate_dict:
      aggregate_dict[name] += score
    else:
      aggregate_dict[name] = score
  max_aggregate = max(aggregate_dict, key=aggregate_dict.get)
  return (max_aggregate, aggregate_dict[max_aggregate])