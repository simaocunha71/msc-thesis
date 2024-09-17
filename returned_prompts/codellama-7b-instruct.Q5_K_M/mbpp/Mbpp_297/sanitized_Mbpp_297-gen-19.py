def flatten_list(list_to_flatten: list) -> list:
  flattened_list = []
  for element in list_to_flatten:
    if isinstance(element, list):
      flattened_list.extend(flatten_list(element))
    else:
      flattened_list.append(element)
  return flattened_list