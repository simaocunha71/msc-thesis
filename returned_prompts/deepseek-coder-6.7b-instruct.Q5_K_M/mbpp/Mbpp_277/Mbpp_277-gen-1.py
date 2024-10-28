
def dict_filter(dic: dict, n: int) -> dict:
  return {k: v for k, v in dic.items() if v >= n}


