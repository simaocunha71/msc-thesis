def common_in_nested_lists(lists: list) -> set:
  return set(list(i for l in lists for i in l))