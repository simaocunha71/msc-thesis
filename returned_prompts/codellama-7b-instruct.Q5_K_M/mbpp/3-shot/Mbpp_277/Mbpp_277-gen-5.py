
def dict_filter(my_dict: dict,n: int) -> dict:
  return {k: v for k, v in my_dict.items() if v >= n}


