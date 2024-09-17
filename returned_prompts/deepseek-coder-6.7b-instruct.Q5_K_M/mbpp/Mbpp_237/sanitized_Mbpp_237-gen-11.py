def check_occurences(lst):
  count_dict = {}
  for tup in lst:
    if tup in count_dict:
      count_dict[tup] += 1
    else:
      count_dict[tup] = 1
  return count_dict