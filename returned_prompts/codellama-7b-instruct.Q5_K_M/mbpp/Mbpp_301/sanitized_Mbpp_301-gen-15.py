def dict_depth(my_dict: dict):
  depth = 1
  for key, value in my_dict.items():
    if isinstance(value, dict):
      depth = max(depth, dict_depth(value)+1)
  return depth