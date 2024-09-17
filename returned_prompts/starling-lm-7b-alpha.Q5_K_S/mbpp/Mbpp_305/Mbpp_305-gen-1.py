
def start_withp(words: list) -> tuple:
  p_words = [word for word in words if word.startswith('p')]
  if len(p_words) >=2:
    return p_words[0], p_words[1]
  else:
    return p_words[0], "No second word found!"


