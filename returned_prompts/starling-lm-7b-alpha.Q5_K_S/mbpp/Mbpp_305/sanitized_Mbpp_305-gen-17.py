def start_withp(words: list) -> str:
  p_words = [word for word in words if word.startswith('p')]
  return tuple(p_words[:2])