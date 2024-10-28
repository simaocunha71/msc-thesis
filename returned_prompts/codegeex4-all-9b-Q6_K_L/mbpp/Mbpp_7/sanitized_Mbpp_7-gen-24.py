def find_char_long(string: str) -> list:
  words = string.split()
  long_words = [word for word in words if len(word) >= 4]
  return long_words