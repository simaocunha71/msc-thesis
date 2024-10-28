def remove_length(string: str, k: int) -> str:
  words = string.split(' ')
  result = []
  for word in words:
    if len(word) != k:
      result.append(word)
  return ' '.join(result)