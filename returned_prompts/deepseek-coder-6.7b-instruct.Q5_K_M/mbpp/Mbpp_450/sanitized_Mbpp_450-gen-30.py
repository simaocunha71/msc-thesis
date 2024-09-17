def extract_string(lst: list,n: int) -> list:
  return [word for word in lst if len(word) > n]