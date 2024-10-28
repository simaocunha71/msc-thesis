
def start_withp(words: list) -> tuple:
  p_words = []
  for word in words:
    if word[0] == 'p':
      p_words.append(word)
  return tuple(p_words)


