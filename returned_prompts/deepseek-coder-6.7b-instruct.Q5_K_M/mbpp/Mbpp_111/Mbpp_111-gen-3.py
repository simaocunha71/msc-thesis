
def common_in_nested_lists(nested_list):
  return set(nested_list[0]).intersection(*nested_list[1:])


