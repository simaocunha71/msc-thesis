def common_in_nested_lists(nested_list):
  common_elements = set(nested_list[0]).intersection(*nested_list[1:])
  return common_elements