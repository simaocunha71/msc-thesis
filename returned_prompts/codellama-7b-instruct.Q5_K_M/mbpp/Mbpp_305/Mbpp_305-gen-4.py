
def start_withp(words: list) -> tuple:
  p_words = [word for word in words if word.split()[0] == 'Python']
  return tuple(p_words[0].split())


