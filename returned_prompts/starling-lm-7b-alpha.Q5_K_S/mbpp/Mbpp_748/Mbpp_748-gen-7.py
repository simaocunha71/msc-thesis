
def capital_words_spaces(word: str) -> str:
  if word[0].islower():
    return word
  else:
    return word[0] + " " + word[1:]


