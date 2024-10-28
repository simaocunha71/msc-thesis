
def find_char_long(s: str) -> set:
  return set(word for word in s.split() if len(word) >= 4)


