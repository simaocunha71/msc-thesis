
def long_words(n, sentence):
  words = sentence.split(" ")
  long_words = [word for word in words if len(word) > n]
  return long_words


