
def remove_length(string: str, length: int) -> str:
  words = string.split()
  new_words = [word for word in words if len(word) != length]
  return " ".join(new_words)


