
def max_length(lst):
  max_len = max(len(sub_list) for sub_list in lst)
  max_list = [sub_list for sub_list in lst if len(sub_list) == max_len]
  return (max_len, max_list[0])


