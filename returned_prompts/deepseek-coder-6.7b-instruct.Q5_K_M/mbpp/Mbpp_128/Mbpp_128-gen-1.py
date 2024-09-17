
def long_words(n: int,text: str) -> list:
  words = text.split()
  return [word for word in words if len(word) > n]


