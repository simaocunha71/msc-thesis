def dict_filter(d: dict, n: int) -> dict:
  return {k: v for k, v in d.items() if v >= n}