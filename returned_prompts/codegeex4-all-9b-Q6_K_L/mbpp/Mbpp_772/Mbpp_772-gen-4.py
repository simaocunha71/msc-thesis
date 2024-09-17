def remove_length(string: str,k: int) -> str:
  words = string.split()
  new_words = [word for word in words if len(word) != k]
  new_string = ' '.join(new_words)
  return new_string

