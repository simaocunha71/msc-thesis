
def find_char_long(s: str) -> set:
  return {word for word in s.split() if len(word) >= 4}


