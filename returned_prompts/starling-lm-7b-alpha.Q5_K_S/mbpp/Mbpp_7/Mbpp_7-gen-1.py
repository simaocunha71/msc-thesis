
def find_char_long(str_in: str) -> set:
  return set(word for word in str_in.split() if len(word) > 3)


