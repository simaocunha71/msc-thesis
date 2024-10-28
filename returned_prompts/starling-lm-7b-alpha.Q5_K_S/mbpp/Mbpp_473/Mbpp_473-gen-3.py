
def tuple_intersection(tup1: list,tup2: list) -> set:
  tup1_set = set(tup1)
  tup2_set = set(tup2)
  intersection = tup1_set & tup2_set
  return intersection


