def max_aggregate(tup_list: list) -> tuple:
  max_tup = tuple(max(tup[0],tup[1]) for tup in tup_list)
  return max_tup