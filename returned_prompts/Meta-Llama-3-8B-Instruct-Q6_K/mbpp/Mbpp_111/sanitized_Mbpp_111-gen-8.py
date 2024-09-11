def common_in_nested_lists(lists):
  common = set(lists[0])
  for lst in lists[1:]:
    common &= set(lst)
  return common