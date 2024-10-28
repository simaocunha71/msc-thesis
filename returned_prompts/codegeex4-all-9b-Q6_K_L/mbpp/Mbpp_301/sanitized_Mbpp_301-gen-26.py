def dict_depth(nested_dict):
  return max(map(dict_depth, nested_dict)) + 1 if isinstance(nested_dict, dict) else 0