def remove_length(string, k: int) -> str:
  words = string.split()
  new_words = [word for word in words if len(word) != k]
  return ' '.join(new_words)