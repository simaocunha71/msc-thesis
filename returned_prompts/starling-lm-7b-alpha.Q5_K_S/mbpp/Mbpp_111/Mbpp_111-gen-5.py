
def common_in_nested_lists(nested_lists:list)->set:
  common_set = set()
  for i in nested_lists:
    common_set |= set(i)
  return common_set


