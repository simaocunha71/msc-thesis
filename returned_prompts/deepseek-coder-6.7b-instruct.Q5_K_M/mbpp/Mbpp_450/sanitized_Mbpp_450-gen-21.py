def extract_string(words: list, n: int) -> list:
  return [word for word in words if len(word) > n]