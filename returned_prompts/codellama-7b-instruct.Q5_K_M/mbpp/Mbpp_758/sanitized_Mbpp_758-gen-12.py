def unique_sublists(my_list):
  unique_sublists = {}
  for sublist in map(tuple, my_list):
    unique_sublists[sublist] = unique_sublists.get(sublist, 0) + 1
  return unique_sublists