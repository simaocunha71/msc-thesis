
def remove_length(string: str, k: int) -> str:
  words = string.split()
  new_words = []
  for word in words:
    if len(word) != k:
      new_words.append(word)
  return ' '.join(new_words)


