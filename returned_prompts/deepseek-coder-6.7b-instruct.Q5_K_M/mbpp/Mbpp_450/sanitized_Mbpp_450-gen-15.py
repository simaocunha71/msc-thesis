def extract_string(lst: list,n: int)  -> list:
  return [i for i in lst if len(i) > n]