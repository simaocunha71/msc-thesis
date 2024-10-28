def start_withp(words: list) -> tuple:
  p_words = [word for word in words if word.startswith('p')]
  return (p_words[0], p_words[1]) if len(p_words) >= 2 else (p_words[0],)


