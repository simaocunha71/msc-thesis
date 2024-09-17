def find_char_long(string: str) -> set:
  return set([word for word in string.split() if len(word) >= 4])