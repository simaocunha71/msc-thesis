
def common_in_nested_lists(nested_list: list):
  common_elements = []
  for i in range(len(nested_list)):
    for j in range(i+1, len(nested_list)):
      common_elements = common_elements + list(set(nested_list[i]) & set(nested_list[j]))
  return list(set(common_elements))


