def merge_dictionaries_three(dict1, dict2, dict3):
  return {**dict1, **dict2, **dict3}  # Python 3.5+
  # for older Python versions:
  # return dict(dict1.items() + dict2.items() + dict3.items())  # Python 3.0-3.4
  # return dict(dict1.items() + [(k, v) for d in [dict2, dict3] for k, v in d.items()])  # Python 2.x