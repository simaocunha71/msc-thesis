def find_char_long(s: str) -> set:
  words = s.split(' ')
  long_words = [word for word in words if len(word) >= 4]
  return set(long_words)