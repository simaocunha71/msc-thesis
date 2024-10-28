def find_char_long(words: str) -> set:
  words = words.split()
  return set(word for word in words if len(word) >= 4)