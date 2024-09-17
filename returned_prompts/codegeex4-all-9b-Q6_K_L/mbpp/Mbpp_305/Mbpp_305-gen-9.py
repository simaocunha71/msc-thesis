def start_withp(words: list) -> tuple:
  start_p = [word for word in words if word.startswith('p')]
  return tuple(start_p)

