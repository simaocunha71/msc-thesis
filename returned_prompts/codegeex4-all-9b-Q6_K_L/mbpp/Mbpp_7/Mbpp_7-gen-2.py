def find_char_long(s: str) -> list:
  words = s.split()
  return [word for word in words if len(word) >= 4]