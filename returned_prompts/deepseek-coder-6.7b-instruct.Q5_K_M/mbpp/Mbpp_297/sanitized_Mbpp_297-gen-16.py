def flatten_list(nested_list):
  flatten_list = []
  for i in nested_list:
    if isinstance(i, list):
      flatten_list.extend(flatten_list(i))
    else:
      flatten_list.append(i)
  return flatten_list