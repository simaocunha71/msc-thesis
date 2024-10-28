
def max_length(list_of_lists):
  max_len = 0
  max_list = []
  for l in list_of_lists:
    if len(l) > max_len:
      max_len = len(l)
      max_list = l
  return (max_len, max_list)


