def capital_words_spaces(word: str) -> str:
  if word[0].isupper():
    return ' ' + word
  return word