def tuple_intersection(tup_list_1: list, tup_list_2: list) -> set:
  set_1 = set()
  for tup in tup_list_1:
    set_1.add(frozenset(tup))

  set_2 = set()
  for tup in tup_list_2:
    set_2.add(frozenset(tup))

  return {frozenset(tup) for tup in set_1 & set_2}