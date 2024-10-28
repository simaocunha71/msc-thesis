def count_Occurrence(tup, lst) -> dict:
  return {i: sum(x == i for x in lst) for i in set(lst)}