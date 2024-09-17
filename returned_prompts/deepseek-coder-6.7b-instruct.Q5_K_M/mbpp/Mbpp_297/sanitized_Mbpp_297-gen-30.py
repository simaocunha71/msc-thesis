def flatten_list(nested_list):
  flat_list = []
  for i in nested_list:
    if isinstance(i, list):
      for j in i:
        flat_list.append(j)
    else:
      flat_list.append(i)
  return flat_list