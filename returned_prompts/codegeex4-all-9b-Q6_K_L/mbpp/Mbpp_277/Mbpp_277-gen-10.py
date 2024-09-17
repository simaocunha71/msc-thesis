def dict_filter(dictionary: dict, n: int) -> dict:
  filtered_dict = {k: v for k, v in dictionary.items() if v >= n}
  return filtered_dict

