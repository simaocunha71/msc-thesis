def find_char_long(s: str) -> list:
  words = s.split()
  long_words = [word for word in words if len(word) >= 4]
  return long_words