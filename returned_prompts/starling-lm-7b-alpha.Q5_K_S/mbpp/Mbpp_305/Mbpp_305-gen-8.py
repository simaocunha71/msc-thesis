
def start_withp(words: list) -> tuple:
  p_words = []
  for w in words:
    if w[0] == 'p':
      p_words.append(w)
  return tuple(p_words)


