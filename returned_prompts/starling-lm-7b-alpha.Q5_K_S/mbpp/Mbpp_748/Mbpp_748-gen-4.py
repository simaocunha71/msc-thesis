
def capital_words_spaces(string: str) -> str:
  if string[0].isupper() and len(string) != 1:
    return string[0] + ' ' + string[1:]
  return string


