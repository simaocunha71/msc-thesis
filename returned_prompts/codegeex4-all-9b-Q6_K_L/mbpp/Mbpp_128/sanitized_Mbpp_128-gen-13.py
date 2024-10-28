def long_words(n: int, words: str) -> list:
  word_list = words.split()
  return [word for word in word_list if len(word) > n]