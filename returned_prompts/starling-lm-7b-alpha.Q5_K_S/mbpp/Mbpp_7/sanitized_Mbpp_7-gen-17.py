def find_char_long(str:str) -> set:
  return set(word for word in str.split() if len(word) >= 4)