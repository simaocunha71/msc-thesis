def unique_sublists(lst):
  counter = {}
  for sublist in lst:
    sublist_tuple = tuple(sublist)
    if sublist_tuple not in counter:
      counter[sublist_tuple] = 1
    else:
      counter[sublist_tuple] += 1
  return counter