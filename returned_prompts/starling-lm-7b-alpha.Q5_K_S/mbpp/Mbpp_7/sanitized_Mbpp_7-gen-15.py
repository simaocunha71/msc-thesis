def find_char_long(text:str) -> set:
  return set(word for word in text.split() if len(word) >= 4)