def long_words(n: int, words: str) -> list:
  long_words = [word for word in words.split() if len(word) > n]
  return long_words