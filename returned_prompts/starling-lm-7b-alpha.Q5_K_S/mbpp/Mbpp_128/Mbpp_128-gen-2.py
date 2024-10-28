
def long_words(n,sentence):
  words = sentence.split()
  long_words = []
  for word in words:
    if len(word) > n:
      long_words.append(word)
  return long_words


