
def dict_depth(my_dict):
  if not isinstance(my_dict, dict):
    return 0
  return 1 + (max(dict_depth(value) for value in my_dict.values()))


