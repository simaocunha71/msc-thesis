
def long_words(n: int, sent: str) -> list:
  words = sent.split(" ")
  long_words = [word for word in words if len(word) > n]
  return long_words


