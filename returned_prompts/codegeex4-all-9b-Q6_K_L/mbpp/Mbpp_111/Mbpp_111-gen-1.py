def common_in_nested_lists(lst):
  common_elements = set(lst[0]).intersection(*lst[1:])
  return common_elements

