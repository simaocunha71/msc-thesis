
def flatten_list(nested_list):
  flattened_list = []
  for i in nested_list:
    if isinstance(i, list):
      flattened_list.extend(flatten_list(i))
    else:
      flattened_list.append(i)
  return flattened_list


