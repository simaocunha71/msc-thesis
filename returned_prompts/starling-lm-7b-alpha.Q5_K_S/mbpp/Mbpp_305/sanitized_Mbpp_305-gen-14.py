def start_withp(words: str) -> str:
  p_words = [word for word in words.split() if word.startswith('p')]
  return (p_words[0], p_words[1])