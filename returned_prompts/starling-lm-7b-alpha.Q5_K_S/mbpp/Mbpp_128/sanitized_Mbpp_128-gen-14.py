def long_words(n, text: str) -> list:
  return [word for word in text.split() if len(word) > n]