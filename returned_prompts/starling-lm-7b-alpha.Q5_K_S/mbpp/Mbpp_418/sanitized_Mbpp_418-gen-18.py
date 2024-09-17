def Find_Max(list_of_strings):
  max_len = 0
  max_str = ""
  for i in list_of_strings:
    if len(i) > max_len:
      max_len = len(i)
      max_str = i
  return max_str