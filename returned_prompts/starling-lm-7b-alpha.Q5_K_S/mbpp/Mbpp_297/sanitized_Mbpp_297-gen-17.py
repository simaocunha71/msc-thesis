def flatten_list(nested_list: list):
  flatten_list = []
  for i in nested_list:
    if type(i) == list:
      flatten_list += flatten_list(i)
    else:
      flatten_list.append(i)
  return flatten_list