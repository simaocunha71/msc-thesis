def reverse_words(string: str) -> str:
  words = string.split(' ')
  reversed_words = [word[::-1] for word in words]
  return ' '.join(reversed_words)