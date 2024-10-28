def long_words(n, string):
  words = string.split(' ')
  long_words = [word for word in words if len(word) > n]
  return long_words

