def reverse_words(s):
  words = s.split()
  return ' '.join(reversed(words))  # or words[::-1] for Python 3.7 and above
  # return ' '.join(reversed(s.split())) for Python 3.6 and below