def long_words(n, words: str) -> list:
  words_list = words.split()
  long_words_list = [word for word in words_list if len(word) > n]
  return long_words_list