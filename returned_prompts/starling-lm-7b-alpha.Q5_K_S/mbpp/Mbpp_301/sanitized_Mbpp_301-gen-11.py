def dict_depth(dictionary: dict) -> int:
  max_depth = 0
  for key, value in dictionary.items():
    if isinstance(value, dict):
      max_depth = max(dict_depth(value), max_depth)
  return max_depth + 1