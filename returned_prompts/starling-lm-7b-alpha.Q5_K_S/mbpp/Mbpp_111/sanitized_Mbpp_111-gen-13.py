def common_in_nested_lists(nested_lists: list) -> set:
  set_common = set()
  for i in nested_lists:
    set_common = set_common | set(i)
  return set_common