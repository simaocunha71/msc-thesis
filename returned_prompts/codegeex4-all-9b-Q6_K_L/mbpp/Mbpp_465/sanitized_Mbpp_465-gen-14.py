def drop_empty(dictionary: dict):
  return {k: v for k, v in dictionary.items() if v is not None}