
def flatten_list(nested_list: list) -> list:
  flattened_list = []
  for item in nested_list:
    if isinstance(item, list):
      flattened_list.extend(item)
    else:
      flattened_list.append(item)
  return flattened_list


