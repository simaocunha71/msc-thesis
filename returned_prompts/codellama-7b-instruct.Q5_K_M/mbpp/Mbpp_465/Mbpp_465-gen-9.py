
def drop_empty(my_dict: dict) -> dict:
  return {key: value for key, value in my_dict.items() if value}


