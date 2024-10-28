
def extract_string(lst: list, size: int) -> list:
  return [word for word in lst if len(word) > size]


