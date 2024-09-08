def Find_Min_Length(list_of_lists):
  min_length = len(list_of_lists[0])
  for lst in list_of_lists:
    if len(lst) < min_length:
      min_length = len(lst)
  return min_length