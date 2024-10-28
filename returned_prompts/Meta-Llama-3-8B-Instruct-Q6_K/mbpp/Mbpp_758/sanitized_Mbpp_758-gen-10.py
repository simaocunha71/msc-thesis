def unique_sublists(lst):
  count_dict = {}
  for sublist in lst:
    sublist_tuple = tuple(sublist)
    if sublist_tuple in count_dict:
      count_dict[sublist_tuple] += 1
    else:
      count_dict[sublist_tuple] = 1
  return count_dict