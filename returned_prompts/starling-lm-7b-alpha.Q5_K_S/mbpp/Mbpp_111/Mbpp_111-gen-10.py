
def common_in_nested_lists(nested_lists:list)->set:
  flat_list = [item for sublist in nested_lists for item in sublist]
  return set(flat_list)


