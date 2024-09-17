def max_length(list_of_lists:list):
  max_length = 0
  max_list = []
  for l in list_of_lists:
    if len(l) > max_length:
      max_length = len(l)
      max_list = l
  return max_length, max_list