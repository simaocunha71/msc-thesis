def check_occurences(tuples_list):
  count_dict = {}
  for tup in tuples_list:
    if tup in count_dict:
      count_dict[tup] += 1
    else:
      count_dict[tup] = 1
  return count_dict