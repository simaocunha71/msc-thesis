def drop_empty(my_dict: dict) -> dict:
  return {k: v for k, v in my_dict.items() if v}