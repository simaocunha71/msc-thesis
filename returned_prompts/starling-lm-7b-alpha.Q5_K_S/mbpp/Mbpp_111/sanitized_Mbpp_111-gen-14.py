def common_in_nested_lists(nested_list: list) -> set:
  common_set = set()
  for l in nested_list:
    common_set = common_set & set(l)
  return common_set