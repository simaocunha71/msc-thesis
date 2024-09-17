
def capital_words_spaces(s: str) -> str:
  words = s.split()
  result = ''
  for word in words:
    result = result + word[0].upper() + word[1:] + ' '
  return result.strip()


