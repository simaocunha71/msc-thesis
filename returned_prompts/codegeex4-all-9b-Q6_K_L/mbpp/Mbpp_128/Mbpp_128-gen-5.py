def long_words(n, word_list: str) -> list:
  long_words = [word for word in word_list.split() if len(word) > n]
  return long_words