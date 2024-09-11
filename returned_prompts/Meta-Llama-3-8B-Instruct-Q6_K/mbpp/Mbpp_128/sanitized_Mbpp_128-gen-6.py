def long_words(n, words):
  return [word for word in words.split() if len(word) > n]  # split the string into words and filter out words with length less than n.