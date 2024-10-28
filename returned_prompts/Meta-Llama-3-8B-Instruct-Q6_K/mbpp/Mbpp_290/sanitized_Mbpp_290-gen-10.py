def max_length(lists):
  max_len = 0
  max_list = []
  for lst in lists:
    if len(lst) > max_len:
      max_len = len(lst)
      max_list = lst
  return (max_len, max_list)  # return a tuple with the max length and the corresponding list