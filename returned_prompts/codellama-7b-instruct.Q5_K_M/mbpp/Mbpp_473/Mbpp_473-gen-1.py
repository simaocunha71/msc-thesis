
def tuple_intersection(tuple_list):
  common_tuple = set()
  for tup in tuple_list:
    common_tuple |= set(tup)
  return common_tuple


