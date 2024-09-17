def check_occurences(tup_list):
  tup_dict = {}
  for tup in tup_list:
    if tup in tup_dict:
      tup_dict[tup] += 1
    else:
      tup_dict[tup] = 1
  return tup_dict