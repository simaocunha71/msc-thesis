def check_occurences(my_list):
  return {k:my_list.count(k) for k in set(my_list)}