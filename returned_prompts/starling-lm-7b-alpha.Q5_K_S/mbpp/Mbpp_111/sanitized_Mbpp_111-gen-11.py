def common_in_nested_lists(nested_lists):
  return set(x for sublist in nested_lists for x in sublist)