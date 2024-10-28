def common_in_nested_lists(nested_lists: list):
  common_set = set()
  for i in range(len(nested_lists)):
    common_set |= set(nested_lists[i])
  return common_set