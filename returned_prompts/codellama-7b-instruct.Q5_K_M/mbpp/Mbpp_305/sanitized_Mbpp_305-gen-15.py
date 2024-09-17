def start_withp(words: list) -> (str, str):
  for word in words:
    if word.split()[0] == 'Python':
      return word.split()[0], word.split()[1]
  return None, None