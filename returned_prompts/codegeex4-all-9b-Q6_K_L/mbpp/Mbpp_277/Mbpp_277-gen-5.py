def dict_filter(dict_nums: dict,n: int) -> dict:
  return {k: v for k, v in dict_nums.items() if v >= n}