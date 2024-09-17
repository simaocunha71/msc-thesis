def max_length(my_list_of_lists):
  max_len = 0
  for lst in my_list_of_lists:
    if len(lst) > max_len:
      max_len = len(lst)
      longest_list = lst
  return (max_len, longest_list)