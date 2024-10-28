def common_in_nested_lists(nested_lists):
  if not nested_lists:
    return set()
  common_elements = set(nested_lists[0])
  for lst in nested_lists[1:]:
    common_elements &= set(lst)
  return common_elements