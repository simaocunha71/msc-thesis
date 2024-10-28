def check_occurences(lst):
  dict_count = {}
  for tup in lst:
    if tup in dict_count:
      dict_count[tup] += 1
    else:
      dict_count[tup] = 1
  return dict_count