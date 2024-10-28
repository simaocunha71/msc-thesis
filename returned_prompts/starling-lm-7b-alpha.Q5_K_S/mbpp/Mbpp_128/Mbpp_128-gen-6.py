
def long_words(n: int, test_str: str) -> list:
  words = test_str.split()
  long_words = [word for word in words if len(word) > n]
  return long_words


