
def tuple_intersection(tuple_list):
  final_set = set()
  for i in tuple_list:
    final_set.update(set(i))
  return set(tuple(i) for i in final_set)


