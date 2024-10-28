def common_in_nested_lists(nested_lists):
  common_elements = set()
  for sublist in nested_lists:
    common_elements.intersection(sublist)
  return list(common_elements)