def long_words(n: int, string: str) -> list:
  words = string.split(" ")
  return [word for word in words if len(word) > n]