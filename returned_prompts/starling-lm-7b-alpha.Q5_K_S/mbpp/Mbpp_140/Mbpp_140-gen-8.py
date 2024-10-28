
def extract_singly(nested_list: list) -> set:
  flatten_list = []
  for i in nested_list:
    flatten_list.extend(i)
  return set(flatten_list)


