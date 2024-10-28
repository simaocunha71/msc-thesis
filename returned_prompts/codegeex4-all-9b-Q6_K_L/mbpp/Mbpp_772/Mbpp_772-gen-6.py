def remove_length(sentence: str, length: int) -> str:
  words = sentence.split()
  filtered_words = [word for word in words if len(word) != length]
  return ' '.join(filtered_words)