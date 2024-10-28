def common_in_nested_lists(nested_lists: list) -> list:
  common_elements = set(nested_lists[0])
  for lst in nested_lists[1:]:
      common_elements = common_elements.intersection(lst)
  return list(common_elements)