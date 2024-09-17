
def find_char_long(sentence: str) -> set:
  return set(x for x in sentence.split() if len(x) >= 4)


