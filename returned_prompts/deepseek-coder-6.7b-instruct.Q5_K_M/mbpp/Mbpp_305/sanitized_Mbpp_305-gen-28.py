def start_withp(words: list) -> tuple:
  for word in words:
    if word.startswith('p'):
      return tuple(word.split())