def merge_dictionaries_three(dict1: dict, dict2: dict, dict3: dict) -> dict:
  merged_dict = {**dict1, **dict2, **dict3}
  return merged_dict